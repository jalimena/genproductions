import os
import fnmatch
import yaml


def find_all_matching(path, pattern):
    if not os.path.exists(path):
        raise RuntimeError("Invalid path '{0}'".format(path))
    result = []
    for root, dirs, files in os.walk(path):
        for thisfile in files:
            if fnmatch.fnmatch(thisfile, pattern):
                result.append(os.path.join(root, thisfile))
    return result


class Variable(object):
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
    def __init__(self, name):
        self.name = name
        self.variables = []

    def add_variable(self, variable):
        self.variables.append(variable)

    def write_yaml(self, outdir="."):
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
    def __init__(self, label):
        self.label = label
        self.is_symmetric = True
        self.values = []
        self.values_up = []
        self.values_down = []
