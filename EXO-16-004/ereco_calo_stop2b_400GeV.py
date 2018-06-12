#!/usr/bin/env python
import os, sys
import numpy as np

if __name__ == '__main__':
    mass = 400
    Etop_400GeV = [98,   111,   141,   189,   210,   231]
    ereco_stop2body_400GeV = [0.1961643,   0.2582864,   0.3270794,   0.3852408,   0.3917032,   0.4067125]
    error_ereco_stop2body_400GeV = [0.006993917,   0.008231059,   0.009512402,   0.01054736,   0.01066024,   0.01092098]

    info  = "independent_variables:\n"
    info += "- header:\n"
    info += "    name: $E_{t}$\n"
    info += "    units: GeV\n"
    info += "  values:\n"
    for v in Etop_400GeV:
        info += "  - value: {0}\n".format(v)

    info += "dependent_variables:\n"

    info += "- header:\n"
    info += "    name: $\\varepsilon_{reco}$\n"
    info += "  qualifiers:\n"
    info += "  - {{value: {0}, name: Top squark mass, units: GeV}}\n".format(mass)
    info += "  values:\n"
    for idx in range(len(Etop_400GeV)):
        v = ereco_stop2body_400GeV[idx]
        v_e = error_ereco_stop2body_400GeV[idx]
        info += "  - value: {0:.6g}\n".format(v)
        info += "    errors:\n"
        info += "    - {{symerror: {0:.6g}, label: 'stat'}}\n".format(v_e)

    with open("ereco_2body_stop400GeV.yaml", "w") as f:
        f.write(info)
