#!/usr/bin/env python
import os, sys
import numpy as np

if __name__ == '__main__':
    mass800 = 800
    mass1000 = 1000

    massDiff_800and1000GeV = [50,   100,   150,   200,   250,   300,   350,   400,   450]
    ereco_gluino3body_800GeV = [0.003522505,   0.3385518,   0.5264188,   0.5518591,   0.5733855,   0.5616438,   0.5772994,   0.5616438,   0.5596869]
    error_ereco_gluino3body_800GeV = [0.0008317234,   0.009417156,   0.01253984,   0.01294583,   0.01328711,   0.0131012,   0.01334895,   0.0131012,   0.01307016]

    ereco_gluino3body_1000GeV = [0.003130755,   0.3462247,   0.519337,   0.572744,   0.5709024,   0.5801105,   0.572744,   0.5561695,   0.5616943]
    error_ereco_gluino3body_1000GeV = [0.0007605073,   0.009264839,   0.01205457,   0.01287981,   0.01285155,   0.01299269,   0.01287981,   0.01262502,   0.01271007]

    info  = "independent_variables:\n"
    info += "- header:\n"
    info += "    name: $m_{\\tilde{g}} - m_{\\tilde{\\chi}^{0}}$\n"
    info += "    units: GeV\n"
    info += "  values:\n"
    for v in massDiff_800and1000GeV:
        info += "  - value: {0}\n".format(v)

    info += "dependent_variables:\n"

    info += "- header:\n"
    info += "    name: $\\varepsilon_{reco}$ ($\\tilde{g} \\rightarrow q\\bar{q}\\tilde{\\chi}^{0}$)\n"
    info += "  qualifiers:\n"
    info += "  - {{value: {0}, name: Gluino mass, units: GeV}}\n".format(mass800)
    info += "  values:\n"
    for idx in range(len(massDiff_800and1000GeV)):
        v = ereco_gluino3body_800GeV[idx]
        v_e = error_ereco_gluino3body_800GeV[idx]
        info += "  - value: {0:.6g}\n".format(v)
        info += "    errors:\n"
        info += "    - {{symerror: {0:.6g}, label: 'stat'}}\n".format(v_e)

    info += "- header:\n"
    info += "    name: $\\varepsilon_{reco}$ ($\\tilde{g} \\rightarrow q\\bar{q}\\tilde{\\chi}^{0})$\n"
    info += "  qualifiers:\n"
    info += "  - {{value: {0}, name: Gluino mass, units: GeV}}\n".format(mass1000)
    info += "  values:\n"
    for idx in range(len(massDiff_800and1000GeV)):
        v = ereco_gluino3body_1000GeV[idx]
        v_e = error_ereco_gluino3body_1000GeV[idx]
        info += "  - value: {0:.6g}\n".format(v)
        info += "    errors:\n"
        info += "    - {{symerror: {0:.6g}, label: 'stat'}}\n".format(v_e)

    with open("ereco_3body_800and1000GeV.yaml", "w") as f:
        f.write(info)
