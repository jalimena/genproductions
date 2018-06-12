#!/usr/bin/env python
import os, sys
import numpy as np

if __name__ == '__main__':

    ### Luminosity
    lumi = 39.0
    signal = "delayedmuon_gdecaymass"

    ### Gather the results
    masses = [400 ,600 ,800 ,1000 ,1200 ,1400 ,1600]
    obs = [0.673218 ,0.494069 ,0.312392 ,0.383811 ,0.416407 ,0.297682 ,0.312144]
    exp = [0.673218 ,0.494069 ,0.312392 ,0.383811 ,0.416407 ,0.297682 ,0.312144]
    up2 = [0.956441 ,0.664413 ,0.436126 ,0.57492 ,0.599222 ,0.432953 ,0.444077]
    up1 = [0.295781 ,0.213956 ,0.14821 ,0.191855 ,0.19779 ,0.143025 ,0.151466]
    dn2 = [0 ,0 ,0 ,0 ,0 ,0 ,0]
    dn1 = [0 ,0 ,0 ,0 ,0 ,0 ,0]
    theory = [94.8 ,9.07 ,1.47 ,0.32 ,0.0836 ,0.0247 ,0.00796]

    to_tev = 1e-3

    info  = "independent_variables:\n"
    info += "- header:\n"
    info += "    name: $\\mathrm{m}_{\\tilde{g}}$\n"
    info += "    units: GeV\n"
    info += "  values:\n"
    for mass in masses:
        info += "  - value: {0}\n".format(mass)

    info += "dependent_variables:\n"

    info += "- header:\n"
    info += "    name: $\\sigma(pp \\rightarrow \\tilde{g}\\tilde{g}) ~\\mathcal{B}(\\tilde{g} \\rightarrow q\\bar{q}\\tilde{\\chi}^{0}_{2}) ~\\mathcal{B}(\\tilde{\\chi}^{0}_{2} \\rightarrow \\mu^{+}\\mu^{-}\\tilde{\\chi}^{0})$\n"
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
    info += "    name: $\\sigma(pp \\rightarrow \\tilde{g}\\tilde{g}) ~\\mathcal{B}(\\tilde{g} \\rightarrow q\\bar{q}\\tilde{\\chi}^{0}_{2}) ~\\mathcal{B}(\\tilde{\\chi}^{0}_{2} \\rightarrow \\mu^{+}\\mu^{-}\\tilde{\\chi}^{0})$\n"
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

    info += "- header:\n"
    info += "    name: $\\sigma(pp \\rightarrow \\tilde{g}\\tilde{g}) ~\\mathcal{B}(\\tilde{g} \\rightarrow q\\bar{q}\\tilde{\\chi}^{0}_{2}) ~\\mathcal{B}(\\tilde{\\chi}^{0}_{2} \\rightarrow \\mu^{+}\\mu^{-}\\tilde{\\chi}^{0})$\n"
    info += "    units: pb\n"
    info += "  qualifiers:\n"
    info += "  - {name: Limit, value: LO prediction}\n"
    #info += "  - {name: SQRT(S), units: GeV, value: 13000}\n"
    #info += "  - {{name: LUMINOSITY, units: 'fb$^{{-1}}$', value: {0}}}\n".format(lumi)
    info += "  values:\n"

    for idx in range( len(obs) ):
        lim = theory[idx]
        info += "  - value: {0:.6g}\n".format(lim)
    #print info.rstrip("\n")

    with open("lim_{0}.yaml".format(signal), "w") as f:
        f.write(info)
