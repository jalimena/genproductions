#!/usr/bin/env python
import os, sys
import numpy as np

if __name__ == '__main__':

    mass = 1800
    massDiff_1800GeV = [75,   100,   125,   175,   225,   275,   325,   375,   425]
    ereco_gluino3body_1800GeV = [0.12992,   0.3488,   0.48,   0.56,   0.5696,   0.5744,   0.584,   0.5632,   0.5648]
    error_ereco_gluino3body_1800GeV = [0.004846429,   0.008676049,   0.01066133,   0.01182269,   0.01196023,   0.01202887,   0.01216589,   0.01186858,   0.0118915]


    info  = "independent_variables:\n"
    info += "- header:\n"
    info += "    name: $m_{\\tilde{g}} - m_{\\tilde{\\chi}^{0}}$\n"
    info += "    units: GeV\n"
    info += "  values:\n"
    for v in massDiff_1800GeV:
        info += "  - value: {0}\n".format(v)

    info += "dependent_variables:\n"

    info += "- header:\n"
    info += "    name: $\\varepsilon_{reco}$ ($\\tilde{g} \\rightarrow q\\bar{q}\\tilde{\\chi}^{0}$)\n"
    info += "  qualifiers:\n"
    info += "  - {{value: {0}, name: Gluino mass, units: GeV}}\n".format(mass)
    info += "  values:\n"
    for idx in range(len(massDiff_1800GeV)):
        v = ereco_gluino3body_1800GeV[idx]
        v_e = error_ereco_gluino3body_1800GeV[idx]
        info += "  - value: {0:.6g}\n".format(v)
        info += "    errors:\n"
        info += "    - {{symerror: {0:.6g}, label: 'stat'}}\n".format(v_e)

    with open("ereco_3body_1800GeV.yaml", "w") as f:
        f.write(info)
