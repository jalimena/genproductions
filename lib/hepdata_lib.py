import os
import fnmatch
import yaml
import ROOT as r


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


class Variable(object):
    """A Variable is a wrapper for a list of values + some meta data."""
    # pylint: disable=too-many-instance-attributes
    # Eight is reasonable in this case.

    def __init__(self, name):
        self.name = name
        self.is_independent = True
        self.is_binned = True

        self.units = ""
        self.values = []
        self.values_low = []
        self.values_high = []
        self.uncertainties = []

    def make_dict(self):
        tmp = {}
        tmp["header"] = {"name": self.name, "units": self.units}

        tmp["values"] = []

        for i in range(len(self.values_low if self.is_binned else self.values)):
            valuedict = {}

            if self.is_binned:
                valuedict["high"] = self.values_high[i]
                valuedict["low"] = self.values_low[i]
            else:
                valuedict["value"] = self.values[i]

            for unc in self.uncertainties:
                if "errors" not in valuedict.keys():
                    valuedict['errors'] = []
                if unc.is_symmetric:
                    valuedict['errors'].append({"symerror": unc.values[i],
                                                "label": unc.label})
                else:
                    valuedict['errors'].append({"asymerror": {"minus": unc.values_down[i],
                                                              "plus": unc.values_up[i]}})
            tmp["values"].append(valuedict)
        return tmp


class Table(object):
    """A table is a collection of variables."""

    def __init__(self, name):
        self.name = name
        self.variables = []

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
        with open(os.path.join(outdir, '{NAME}.yaml'.format(NAME=self.name)), 'w') as outfile:
            yaml.dump(table, outfile, default_flow_style=False)


class Uncertainty(object):
    """
    Store information about an uncertainty on a variable

    Uncertainties can be symmetric or asymmetric.
    The main information is stored as one (two) lists in the symmetric (asymmetric) case.
    The list entries are the uncertainty for each of the list entries in the corresponding Variable.
    """

    def __init__(self, label):
        self.label = label
        self.is_symmetric = True
        self.values = []
        self.values_up = []
        self.values_down = []


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
                "RootReader: Encountered type of variable passed as tfile argument: " + type(tfile))

        if(not self.tfile):
            raise IOError("RootReader: File not opened properly.")

    def read_graph(self, path_to_graph):
        """Extract lists of X and Y values from a TGraph"""
        graph = self.tfile.Get(path_to_graph)

        points = {"x": [], "y": []}

        for i in range(graph.GetN()):
            x = r.Double()
            y = r.Double()
            graph.GetPoint(i, x, y)
            points["x"].append(float(x))
            points["y"].append(float(y))

        return points
