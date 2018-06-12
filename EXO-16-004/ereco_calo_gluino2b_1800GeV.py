#!/usr/bin/env python
import os, sys
import numpy as np

if __name__ == '__main__':
    mass = 1800
    Egluon_1800GeV = [250,   300,   350,   400,   450,   500]
    ereco_gluino2body_1800GeV = [0.5585081,   0.5371388,   0.5298544,   0.5296943,   0.5335361,   0.5232863]
    error_ereco_gluino2body_1800GeV = [0.01180412,   0.01404263,   0.01139115,   0.01138883,   0.0114444,   0.01379777]

    info  = "independent_variables:\n"
    info += "- header:\n"
    info += "    name: $E_{g}$\n"
    info += "    units: GeV\n"
    info += "  values:\n"
    for v in Egluon_1800GeV:
        info += "  - value: {0}\n".format(v)

    info += "dependent_variables:\n"

    info += "- header:\n"
    info += "    name: $\\varepsilon_{reco}$\n"
    info += "  qualifiers:\n"
    info += "  - {{value: {0}, name: Gluino mass, units: GeV}}\n".format(mass)
    info += "  values:\n"
    for idx in range(len(Egluon_1800GeV)):
        v = ereco_gluino2body_1800GeV[idx]
        v_e = error_ereco_gluino2body_1800GeV[idx]
        info += "  - value: {0:.6g}\n".format(v)
        info += "    errors:\n"
        info += "    - {{symerror: {0:.6g}, label: 'stat'}}\n".format(v_e)

    with open("ereco_2body_gluino1800GeV.yaml", "w") as f:
        f.write(info)
