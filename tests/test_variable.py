#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import sys
from hepdata_lib import *
from test_utilities import *
import numpy as np
import random


def test_variable_scale_binned():
    values = zip(range(0, 5, 1), range(1, 6, 1))

    testvar = Variable("testvar")
    testvar.is_binned = True
    testvar.units = "GeV"
    testvar.values = values

    assert(testvar.values == values)

    for factor in [random.uniform(0, 10000) for x in range(100)]:
        # Check that scaling works
        testvar.scale_values(factor)
        scaled_values = [(factor * x[0], factor * x[1]) for x in values]
        assert(all(tuple_compare(x, y)
                   for x, y in zip(testvar.values, scaled_values)))

        # Check that inverse also works
        testvar.scale_values(1. / factor)
        assert(all(tuple_compare(x, y)
                   for x, y in zip(testvar.values, values)))

    return True


def test_variable_scale_uncertainty():
    values = range(0, 300, 1)
    uncertainty = [x + random.uniform(0, 2) for x in values]

    testvar = Variable("testvar")
    testvar.is_binned = False
    testvar.units = "GeV"
    testvar.values = values

    testunc = Uncertainty("testunc")
    testunc.is_symmetric = True
    testunc.values = uncertainty
    testvar.uncertainties.append(testunc)

    assert(testvar.values == values)
    assert(testunc.values == uncertainty)

    for factor in [random.uniform(0, 10000) for x in range(100)]:
        # Check that scaling works
        testvar.scale_values(factor)
        scaled_values = [factor * x for x in values]
        scaled_uncertainty = [factor * x for x in uncertainty]
        assert(all(float_compare(x, y)
                   for x, y in zip(testvar.values, scaled_values)))
        assert(all(float_compare(x, y)
                   for x, y in zip(testunc.values, scaled_uncertainty)))

        # Check that inverse also works
        testvar.scale_values(1. / factor)
        assert(all(float_compare(x, y)
                   for x, y in zip(testvar.values, values)))
        assert(all(float_compare(x, y)
                   for x, y in zip(testunc.values, uncertainty)))

    return True


def main():
    functions = []
    functions.append(test_variable_scale_binned)
    functions.append(test_variable_scale_uncertainty)

    do_test(functions)


if __name__ == '__main__':
    main()
