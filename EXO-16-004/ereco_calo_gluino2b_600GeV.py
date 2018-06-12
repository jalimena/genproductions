#!/usr/bin/env python
import os, sys
import numpy as np

if __name__ == '__main__':
    mass = 600
    Egluon_600GeV = [50,   75,   85,   95,   105,   150,   195,   220]
    ereco_gluino2body_600GeV = [0.00445269,   0.1512059,   0.2589982,   0.3237477,   0.3916512,   0.5144712,   0.544898,   0.5391465]
    error_ereco_gluino2body_600GeV = [0.0009109228,   0.005682854,   0.007777974,   0.008916852,   0.01005589,   0.01202311,   0.01249721,   0.01240792]

    info  = "independent_variables:\n"
    info += "- header:\n"
    info += "    name: $E_{g}$\n"
    info += "    units: GeV\n"
    info += "  values:\n"
    for v in Egluon_600GeV:
        info += "  - value: {0}\n".format(v)

    info += "dependent_variables:\n"

    info += "- header:\n"
    info += "    name: $\\varepsilon_{reco}$\n"
    info += "  qualifiers:\n"
    info += "  - {{value: {0}, name: Gluino mass, units: GeV}}\n".format(mass)
    info += "  values:\n"
    for idx in range(len(Egluon_600GeV)):
        v = ereco_gluino2body_600GeV[idx]
        v_e = error_ereco_gluino2body_600GeV[idx]
        info += "  - value: {0:.6g}\n".format(v)
        info += "    errors:\n"
        info += "    - {{symerror: {0:.6g}, label: 'stat'}}\n".format(v_e)

    with open("ereco_2body_gluino600GeV.yaml", "w") as f:
        f.write(info)
