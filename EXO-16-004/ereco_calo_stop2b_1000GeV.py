#!/usr/bin/env python
import os, sys
import numpy as np

if __name__ == '__main__':
    mass = 1000
    Etop_1000GeV = [250,   300,   351,   400,   450,   500]
    ereco_stop2body_1000GeV = [0.4080856,   0.4072838,   0.4023781,   0.4009512,   0.3790725,   0.3940547]
    error_ereco_stop2body_1000GeV = [0.0116898,   0.01318899,   0.01158422,   0.01155778,   0.01114992,   0.01142971]

    info  = "independent_variables:\n"
    info += "- header:\n"
    info += "    name: $E_{t}$\n"
    info += "    units: GeV\n"
    info += "  values:\n"
    for v in Etop_1000GeV:
        info += "  - value: {0}\n".format(v)

    info += "dependent_variables:\n"

    info += "- header:\n"
    info += "    name: $\\varepsilon_{reco}$\n"
    info += "  qualifiers:\n"
    info += "  - {{value: {0}, name: Top squark mass, units: GeV}}\n".format(mass)
    info += "  values:\n"
    for idx in range(len(Etop_1000GeV)):
        v = ereco_stop2body_1000GeV[idx]
        v_e = error_ereco_stop2body_1000GeV[idx]
        info += "  - value: {0:.6g}\n".format(v)
        info += "    errors:\n"
        info += "    - {{symerror: {0:.6g}, label: 'stat'}}\n".format(v_e)

    with open("ereco_2body_stop1000GeV.yaml", "w") as f:
        f.write(info)
