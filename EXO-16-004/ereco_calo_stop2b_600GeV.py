#!/usr/bin/env python
import os, sys
import numpy as np

if __name__ == '__main__':
    mass = 600
    Etop_600GeV = [99,   192,   251,   299]
    ereco_stop2body_600GeV = [0.2031917,   0.3872781,   0.4093055,   0.3962688]
    error_ereco_stop2body_600GeV = [0.007412918,   0.0109891,   0.01138663,   0.01115188]

    info  = "independent_variables:\n"
    info += "- header:\n"
    info += "    name: $E_{t}$\n"
    info += "    units: GeV\n"
    info += "  values:\n"
    for v in Etop_600GeV:
        info += "  - value: {0}\n".format(v)

    info += "dependent_variables:\n"

    info += "- header:\n"
    info += "    name: $\\varepsilon_{reco}$\n"
    info += "  qualifiers:\n"
    info += "  - {{value: {0}, name: Top squark mass, units: GeV}}\n".format(mass)
    info += "  values:\n"
    for idx in range(len(Etop_600GeV)):
        v = ereco_stop2body_600GeV[idx]
        v_e = error_ereco_stop2body_600GeV[idx]
        info += "  - value: {0:.6g}\n".format(v)
        info += "    errors:\n"
        info += "    - {{symerror: {0:.6g}, label: 'stat'}}\n".format(v_e)

    with open("ereco_2body_stop600GeV.yaml", "w") as f:
        f.write(info)
