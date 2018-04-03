import os
import fnmatch
import yaml
import ROOT as r
from collections import defaultdict
import math

# Register defalut dict so that yaml knows it is a dictionary type
from yaml.representer import Representer
yaml.add_representer(defaultdict, Representer.represent_dict)


def find_all_matching(path, pattern):
    """Utility function that works like 'find' in bash."""
    if not os.path.exists(path):
        raise RuntimeError("Invalid path '{0}'".format(path))
    result = []
    for root, dirs, files in os.walk(path):
        for thisfile in files:
            if fnmatch.fnmatch(thisfile, pattern):
                result.append(os.path.join(root, thisfile))
    return result


def relative_round(value, relative_digits):
    """Rounds to a given relative precision"""
    if(value == 0):
        return 0
    if(type(value) == str):
        return value
    value_precision = math.ceil(math.log10(abs(value)))

    absolute_digits = - value_precision + relative_digits
    if(absolute_digits < 0):
        absolute_digits = 0

    return round(value, int(absolute_digits))


class Variable(object):
    """A Variable is a wrapper for a list of values + some meta data."""
    # pylint: disable=too-many-instance-attributes
    # Eight is reasonable in this case.

    def __init__(self, name, is_independent=True, is_binned=True, units=""):
        self.name = name
        self.is_independent = is_independent
        self.is_binned = is_binned

        self.units = units
        self.values = []
        self.uncertainties = []
        self.digits = 5

    def set_values(self, values):
        if(self.is_binned):
            self._values = map(lambda x: (float(x[0]), float(x[1])), values)
        else:
            self._values = map(lambda x: x if type(x) ==
                               str else float(x), values)

    def get_values(self):
        return self._values

    values = property(get_values, set_values)

    def scale_values(self, factor):
        """Multiply each value by constant factor. Also applies to uncertainties."""
        if(not self.is_binned):
            self.set_values([factor * x for x in self.get_values()])
        else:
            self.set_values([(factor * x[0], factor * x[1])
                             for x in self.get_values()])

        for unc in self.uncertainties:
            unc.scale_values(factor)

    def make_dict(self):
        tmp = {}
        tmp["header"] = {"name": self.name, "units": self.units}

        tmp["values"] = []

        for i in range(len(self.values)):
            valuedict = defaultdict(list)

            if self.is_binned:
                valuedict["low"] = relative_round(
                    self.values[i][0], self.digits)
                valuedict["high"] = relative_round(
                    self.values[i][1], self.digits)
            else:
                valuedict["value"] = relative_round(
                    self.values[i], self.digits)

            for unc in self.uncertainties:
                if unc.is_symmetric:
                    valuedict['errors'].append({"symerror": relative_round(unc.values[i], self.digits),
                                                "label": unc.label})
                else:
                    valuedict['errors'].append({"asymerror": {"minus": relative_round(unc.values[i][0], self.digits),
                                                              "plus": relative_round(unc.values[i][1], self.digits)},
                                                "label": unc.label})
            tmp["values"].append(valuedict)
        return tmp


class Table(object):
    """
    A table is a collection of variables.

    It also holds meta-data such as a general description,
    the location within the paper, etc.
    """

    def __init__(self, name):
        self.name = name
        self.variables = []
        self.description = "Example description"
        self.location = "Example location"
        self.keywords = {}

    def add_variable(self, variable):
        """Add a variable to the table"""
        self.variables.append(variable)

    def write_yaml(self, outdir="."):
        """Write the table (and all its variables) to a YAML file."""
        # Put all variables together into a table and write
        table = {}
        table["independent_variables"] = []
        table["dependent_variables"] = []
        for var in self.variables:
            table["independent_variables" if var.is_independent else "dependent_variables"].append(
                var.make_dict())

        if not os.path.exists(outdir):
            os.makedirs(outdir)

        shortname = self.name.lower().replace(" ", "-")
        outfile_path = os.path.join(
            outdir, '{NAME}.yaml'.format(NAME=shortname))
        with open(outfile_path, 'w') as outfile:
            yaml.dump(table, outfile, default_flow_style=False)

        # Add entry to central submission file
        submission_path = os.path.join(outdir, 'submission.yaml')
        with open(submission_path, 'a+') as submissionfile:

            submission = {}
            submission["name"] = self.name
            submission["description"] = self.description
            submission["location"] = self.location
            submission["data_file"] = '{NAME}.yaml'.format(NAME=shortname)
            submission["keywords"] = []

            for name, values in self.keywords.items():
                submission["keywords"].append({"name": name, "values": values})

            if(len(submissionfile.read())):
                submissionfile.write("---\n")
            yaml.dump(submission, submissionfile, default_flow_style=False)
        return os.path.basename(outfile_path)


class Submission(object):
    """
    Top-level object of a HEPData submission.

    Holds all the lower-level objects and controls writing.
    """

    def __init__(self):
        self.tables = []
        self.comment = ""

    def add_table(self, table):
        self.tables.append(table)

    def read_abstract(self, filepath):
        with open(filepath) as afile:
            raw = str(afile.read())
        raw = raw.replace("\r\n", "")
        raw = raw.replace("\n", "")

        self.comment = raw

    def create_files(self, outdir="."):
        if not os.path.exists(outdir):
            os.makedirs(outdir)

        # Write general info about submission
        submission = {}
        submission["comment"] = self.comment
        with open(os.path.join(outdir, 'submission.yaml'), 'w') as outfile:
            yaml.dump(submission, outfile, default_flow_style=False)

        # Write all the tables
        for table in self.tables:
            table.write_yaml(outdir)

        # Put everything into a tarfile
        import tarfile
        tar = tarfile.open("submission.tar.gz", "w:gz")
        for f in find_all_matching(outdir, "*.yaml"):
            tar.add(f)
        tar.close()


class Uncertainty(object):
    """
    Store information about an uncertainty on a variable

    Uncertainties can be symmetric or asymmetric.
    The main information is stored as one (two) lists in the symmetric (asymmetric) case.
    The list entries are the uncertainty for each of the list entries in the corresponding Variable.
    """

    def __init__(self, label, is_symmetric=True):
        self.label = label
        self.is_symmetric = is_symmetric
        self.values = []

    def set_values(self, values, nominal=None):
        """
        Setter method

        Can perform list subtraction relative to nominal value.
        """
        if(nominal):
            tmp = []
            for (down, up), nominal in zip(values, nominal):
                tmp.append((down - nominal, up - nominal))
            self._values = tmp
        else:
            if(not self.is_symmetric):
                try:
                    assert(all([x[1] >= 0 for x in values]))
                    assert(all([x[0] <= 0 for x in values]))
                except AssertionError:
                    raise ValueError(
                        "Uncertainty::set_values: Wrong signs detected! First element of uncertainty tuple should be <=0, second >=0.")

            self._values = values

    def get_values(self):
        return self._values
    values = property(get_values, set_values)

    def scale_values(self, factor):
        """Multiply each value by constant factor."""
        if(self.is_symmetric):
            self.set_values([factor * x for x in self.get_values()])
        else:
            self.set_values([(factor * x[0], factor * x[1])
                             for x in self.get_values()])


class RootFileReader(object):
    """Easily extract information from ROOT histograms, graphs, etc"""

    def __init__(self, tfile):
        self.set_file(tfile)

    def __del__(self):
        if(self.tfile):
            self.tfile.Close()

    def set_file(self, tfile):
        """Define the TFile we should read from."""
        if(type(tfile) == str):
            if(os.path.exists(tfile) and tfile.endswith(".root")):
                self.tfile = r.TFile(tfile)
            else:
                raise IOError("RootReader: File does not exist: " + tfile)
        elif(type(tfile) == r.TFile):
            self.tfile = tfile
        else:
            raise ValueError(
                "RootReader: Encountered unkonown type of variable passed as tfile argument: " + type(tfile))

        if(not self.tfile):
            raise IOError("RootReader: File not opened properly.")

    def retrieve_object(self,path_to_object):
        """
        Generalized function to retrieve a TObject from a file.

        There are two use cases:
        1)  The object is saved under the exact path given.
            In this case, the function behaves identically to TFile::Get.

        2)  The object is saved as a primitive in a TCanvas.
            In this case, the path has to be formatted as
            PATH_TO_CANVAS/NAME_OF_PRIMITIVE
        """
        obj = self.tfile.Get(path_to_object)

        # If the Get operation was successful, just return
        # Otherwise, try canvas approach
        if(obj):
            return obj
        else:
            parts = path_to_object.split("/")
            path_to_canvas = "/".join(parts[0:-1])
            name = parts[-1]

            try:
                canv = self.tfile.Get(path_to_canvas)
                assert(canv)
                for entry in list(canv.GetListOfPrimitives()):
                    if(entry.GetName() == name):
                        return entry

                # Didn't find anything. Print available primitives to help user debug.
                print "Available primitives in TCanvas '{0}':".format(path_to_canvas)
                for entry in list(canv.GetListOfPrimitives()):
                    print "Name: '{0}', Type: '{1}'.".format(entry.GetName(),type(entry))
                assert(False)

            except AssertionError:
                raise IOError("Cannot find any object in file {0} with path {1}".format(self.tfile,path_to_object))

    def read_graph(self, path_to_graph):
        """Extract lists of X and Y values from a TGraph."""
        graph = self.retrieve_object(path_to_graph)
        return get_graph_points(graph)



    def read_hist_2d(self,path_to_hist):
        hist = self.retrieve_object(path_to_hist)
        return get_hist_2d_points(hist)


    def read_tree(self, path_to_tree, branchname):
        """Extract a list of values from a tree branch."""
        tree = self.tfile.Get(path_to_tree)

        values = []
        for event in tree:
            values.append(getattr(event, branchname))
        return values


def get_hist_2d_points(hist):
    points = defaultdict(list)
    for ix in range(1,hist.GetNbinsX()+1):
        x = hist.GetXaxis().GetBinCenter(ix)
        for iy in range(1,hist.GetNbinsY()+1):
            y = hist.GetYaxis().GetBinCenter(iy)
            z = hist.GetBinContent(ix,iy)
            points["x"].append(x)
            points["y"].append(y)
            points["z"].append(z)
    return points

def get_graph_points(graph):
    """
    Extract lists of X and Y values from a TGraph.

    A dictionary is returned with the following key-value pairs:

    key "x" -> value list of x values
    key "y" -> value list of y values

    If the input graph is a TGraphErrors (TGraphAsymmErrors), the dictionary also contains


    key "dx" -> value list of x uncertainties (tuple of lower, upper uncertainty)
    key "dy" -> value list of y uncertainties (tuple of lower, upper uncertainty)

    """

    # Check input
    if( type(graph) not in [r.TGraph, r.TGraphErrors, r.TGraphAsymmErrors, r.TGraph2D]):
        raise TypeError("Expected to input to be TGraph or similar, instead got '{0}'".format(type(graph)))

    # Extract points
    points = defaultdict(list)

    # Central value
    points["x"] = list(graph.GetX())
    points["y"] = list(graph.GetY())
    if(type(graph)==r.TGraph2D):
        points["z"] = list(graph.GetZ())

    # For uncertainties, we do not use the inbuilt Get commands
    # because they can give segmentation faults
    if(type(graph)==r.TGraphErrors):
        for i in range(graph.GetN()):
            points["dx"].append(graph.GetErrorX(i))
            points["dy"].append(graph.GetErrorY(i))

    elif(type(graph)==r.TGraphAsymmErrors):
        for i in range(graph.GetN()):
            points["dx"].append((-graph.GetErrorXlow(i),graph.GetErrorXhigh(i)))
            points["dy"].append((-graph.GetErrorYlow(i),graph.GetErrorYhigh(i)))

    return points
