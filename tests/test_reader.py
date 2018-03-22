from hepdata_lib import *
from test_utilities import *
import ROOT as r
import os
import sys
import random

def test_retrieve_object():
    # The test file contains a canvas of name "c1", which is directly accessible
    # The canvas in turn contains a TH2D with name "correlation"
    path =  os.path.join(os.path.dirname(__file__), "testfiles/correlation.root")

    reader = RootFileReader(path)

    # Check direct retrieval of stored object
    c1 = reader.retrieve_object("c1")
    assert( type(c1) == r.TCanvas )
    assert( c1.GetName() == "c1" )

    # Check that object persists even after file closes
    reader.tfile.Close()
    assert( type(c1) == r.TCanvas )
    assert( c1.GetName() == "c1" )

    reader = RootFileReader(path)

    # Check retrieval from canvas primitives
    h2d = reader.retrieve_object("c1/correlation")
    assert(type(h2d)==r.TH2D)
    assert(h2d.GetName() == "correlation")

    # Check that object persists even after file closes
    reader.tfile.Close()
    assert(type(h2d)==r.TH2D)
    assert(h2d.GetName() == "correlation")
    
    return True


def main():
    functions = []
    functions.append(test_retrieve_object)

    do_test(functions)

if __name__ == '__main__':
    main()

