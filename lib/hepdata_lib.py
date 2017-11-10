import os
import fnmatch
def find_all_matching(path,pattern):
    if not os.path.exists(path):
        raise RuntimeError("Invalid path '{0}'".format(path))
    result = []
    for root, dirs, files in os.walk(path):
        for thisfile in files:
            if fnmatch.fnmatch(thisfile, pattern):
                result.append(os.path.join(root, thisfile ))
    return result


class Variable():
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
        tmp["header"]={"name":self.name, "units" : self.units}
        #~ tmp["qualifiers"]=[{ "name" : "TESTQUALNAME", "value":"TESTQUALVALUE" }]
        
        tmp["values"]=[]
        
        for i in range(len(self.values_low if self.is_binned else self.values)):
            valuedict = {}

            if(self.is_binned):
                valuedict["high"] = self.values_high[i]
                valuedict["low"]  = self.values_low[i]
            else:
                valuedict["value"] = self.values[i]

            for unc in self.uncertainties:
                if( not "errors" in valuedict.keys() ): valuedict['errors'] = []
                if unc.is_symmetric:
                    valuedict['errors'].append( { "symerror" : unc.values[i],
                                                  "label" : unc.label})
                else:
                    valuedict['errors'].append( { "asymerror" : { "minus" : unc.values_down[i],
                                                                  "plus" : unc.values_up[i]}})
            tmp["values"].append(valuedict)
        return tmp

class Uncertainty():
    def __init__(self,label):
        self.label = label
        self.is_symmetric = True
        self.values = []
        self.values_up = []
        self.values_down = []
