#!/usr/bin/env python
import os, sys
import numpy as np

if __name__ == '__main__':
    mass = 1200
    Egluon_1200GeV = [50,   75,   85,   95,   105,   145,   185,   220,   260,   300]
    ereco_gluino2body_1200GeV = [0.004325747,   0.1489562,   0.2501411,   0.3447433,   0.400978,   0.5236036,   0.5473011,   0.5493699,   0.5461727,   0.5476773]
    error_ereco_gluino2body_1200GeV = [0.0009039295,   0.005673456,   0.007668999,   0.009337579,   0.0102788,   0.01224909,   0.01262023,   0.01265251,   0.01260261,   0.0126261]

    info  = "independent_variables:\n"
    info += "- header:\n"
    info += "    name: $E_{g}$\n"
    info += "    units: GeV\n"
    info += "  values:\n"
    for v in Egluon_1200GeV:
        info += "  - value: {0}\n".format(v)

    info += "dependent_variables:\n"

    info += "- header:\n"
    info += "    name: $\\varepsilon_{reco}$\n"
    info += "  qualifiers:\n"
    info += "  - {{value: {0}, name: Gluino mass, units: GeV}}\n".format(mass)
    info += "  values:\n"
    for idx in range(len(Egluon_1200GeV)):
        v = ereco_gluino2body_1200GeV[idx]
        v_e = error_ereco_gluino2body_1200GeV[idx]
        info += "  - value: {0:.6g}\n".format(v)
        info += "    errors:\n"
        info += "    - {{symerror: {0:.6g}, label: 'stat'}}\n".format(v_e)

    with open("ereco_2body_gluino1200GeV.yaml", "w") as f:
        f.write(info)
