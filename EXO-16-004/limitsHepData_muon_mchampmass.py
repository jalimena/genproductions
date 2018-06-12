#!/usr/bin/env python
import os, sys
import numpy as np

if __name__ == '__main__':

    ### Luminosity
    lumi = 39.0
    signal = "delayedmuon_mchampdecaymass"

    ### Gather the results
    masses = [100 ,200 ,400 ,600 ,800]
    obs = [0.103949 ,0.0165526 ,0.015724 ,0.0186522 ,0.0169904]
    exp = [0.103949 ,0.0165526 ,0.015724 ,0.0186522 ,0.0169904]
    up2 = [0.14427 ,0.0241696 ,0.0225709 ,0.0271925 ,0.0257318]
    up1 = [0.0476074 ,0.00775436 ,0.00762972 ,0.00890453 ,0.00843517]
    dn2 = [0 ,0 ,0 ,0 ,0]
    dn1 = [0 ,0 ,0 ,0 ,0]
    theory = [3.77794 ,0.298653 ,0.0230997 ,0.00346512 ,0.000796963]

    to_tev = 1e-3

    info  = "independent_variables:\n"
    info += "- header:\n"
    info += "    name: $\\mathrm{m}_{\\mathrm{MCHAMP}}$\n"
    info += "    units: GeV\n"
    info += "  values:\n"
    for mass in masses:
        info += "  - value: {0}\n".format(mass)

    info += "dependent_variables:\n"

    info += "- header:\n"
    info += "    name: $\\sigma(pp \\rightarrow \\mathrm{MCHAMP}~\\mathrm{MCHAMP}) ~\\mathcal{B}(\\mathrm{MCHAMP} \\rightarrow \\mu^{\\pm}\\mu^{\\pm})$\n"
    info += "    units: pb\n"
    info += "  qualifiers:\n"
    info += "  - {name: Limit, value: Observed}\n"
    #info += "  - {name: SQRT(S), units: GeV, value: 13000}\n"
    info += "  - {{name: LUMINOSITY, units: 'fb$^{{-1}}$', value: {0}}}\n".format(lumi)
    info += "  values:\n"

    for idx in range( len(obs) ):
        lim = obs[idx]
        info += "  - value: {0:.6g}\n".format(lim)

    info += "- header:\n"
    info += "    name: $\\sigma(pp \\rightarrow \\mathrm{MCHAMP}~\\mathrm{MCHAMP}) ~\\mathcal{B}(\\mathrm{MCHAMP} \\rightarrow \\mu^{\\pm}\\mu^{\\pm})$\n"
    info += "    units: pb\n"
    info += "  qualifiers:\n"
    info += "  - {name: Limit, value: Expected}\n"
    #info += "  - {name: SQRT(S), units: GeV, value: 13000}\n"
    info += "  - {{name: LUMINOSITY, units: 'fb$^{{-1}}$', value: {0}}}\n".format(lumi)
    info += "  values:\n"

    for idx in range( len(exp) ):
        lim = exp[idx]
        lim_dn1 = dn1[idx]
        lim_dn2 = dn2[idx]
        lim_up1 = up1[idx]
        lim_up2 = up2[idx]
        info += "  - value: {0:.6g}\n".format(lim)
        info += "    errors:\n"
        info += "    - {{asymerror: {{plus: {0:.6g}, minus: {1:.6g}}}, label: '1 sigma'}}\n".format(lim_up1, -lim_dn1)
        info += "    - {{asymerror: {{plus: {0:.6g}, minus: {1:.6g}}}, label: '2 sigma'}}\n".format(lim_up2, -lim_dn2)

    #print info.rstrip("\n")
    info += "- header:\n"
    info += "    name: $\\sigma(pp \\rightarrow \\mathrm{MCHAMP}~\\mathrm{MCHAMP}) ~\\mathcal{B}(\\mathrm{MCHAMP} \\rightarrow \\mu^{\\pm}\\mu^{\\pm})$\n"
    info += "    units: pb\n"
    info += "  qualifiers:\n"
    info += "  - {name: Limit, value: LO prediction}\n"
    #info += "  - {name: SQRT(S), units: GeV, value: 13000}\n"
    #info += "  - {{name: LUMINOSITY, units: 'fb$^{{-1}}$', value: {0}}}\n".format(lumi)
    info += "  values:\n"

    for idx in range( len(obs) ):
        lim = theory[idx]
        info += "  - value: {0:.6g}\n".format(lim)

    with open("lim_{0}.yaml".format(signal), "w") as f:
        f.write(info)
