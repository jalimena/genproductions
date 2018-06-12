#!/usr/bin/env python
import os, sys
import numpy as np

if __name__ == '__main__':

    ### Luminosity
    lumi = 39.0
    signal = "delayedmuon_mchampdecay"

    ### Gather the results
    lifetimes = ['7.5e-08', '1.0e-07', '2.0e-07', '5.0e-07', '7.0e-07', '1.0e-06', '2.0e-06', '5.0e-06', '7.0e-06', '1.0e-05', '3.0e-05', '4.0e-05', '5.0e-05', '7.0e-05', '1.0e-04', '2.0e-04', '5.0e-04', '7.0e-04', '1.0e-03', '6.0e-03', '1.0e-02', '1.0e+01', '5.0e+02', '1.0e+03', '2.0e+03', '3.6e+03', '1.0e+04', '2.0e+04', '5.0e+04', '7.0e+04', '1.0e+05', '2.0e+05', '5.0e+05', '7.0e+05', '1.0e+06']
    obs = [0.300131 ,0.175866 ,0.0741903 ,0.0326474 ,0.0256134 ,0.0223336 ,0.019099 ,0.0170854 ,0.0160943 ,0.0156899 ,0.0156287 ,0.0156287 ,0.0156495 ,0.0155896 ,0.015606 ,0.0156153 ,0.0156166 ,0.0155164 ,0.0156165 ,0.0155896 ,0.01554 ,0.015606 ,0.0156011 ,0.0155788 ,0.015533 ,0.0167188 ,0.0182055 ,0.020314 ,0.024566 ,0.0261905 ,0.0270732 ,0.0293312 ,0.0342744 ,0.0364921 ,0.0394494]
    exp = [0.300131 ,0.175866 ,0.0741903 ,0.0326474 ,0.0256134 ,0.0223336 ,0.019099 ,0.0170854 ,0.0160943 ,0.0156899 ,0.0156287 ,0.0156287 ,0.0156495 ,0.0155896 ,0.015606 ,0.0156153 ,0.0156166 ,0.0155164 ,0.0156165 ,0.0155896 ,0.01554 ,0.015606 ,0.0156011 ,0.0155788 ,0.015533 ,0.0167188 ,0.0182055 ,0.020314 ,0.024566 ,0.0261905 ,0.0270732 ,0.0293312 ,0.0342744 ,0.0364921 ,0.0394494]
    up2 = [0.249711 ,0.101686 ,0.0392176 ,0.033922 ,0.0250865 ,0.0227001 ,0.0264384 ,0.0240694 ,0.0244366 ,0.0236764 ,0.0223813 ,0.0224907 ,0.022621 ,0.0223989 ,0.0223654 ,0.0224734 ,0.0222623 ,0.0227287 ,0.0224076 ,0.0223819 ,0.0224232 ,0.0224017 ,0.0222747 ,0.0233361 ,0.0240785 ,0.0236354 ,0.0268952 ,0.0294971 ,0.0331906 ,0.0344833 ,0.0368775 ,0.0432756 ,0.0513122 ,0.0531392 ,0.0555722]
    up1 = [0 ,0 ,0 ,0.0170674 ,0.0123396 ,0.0107016 ,0.00813813 ,0.00787395 ,0.00802362 ,0.00767729 ,0.00737346 ,0.00747819 ,0.00745569 ,0.00757653 ,0.00756015 ,0.00748988 ,0.00748564 ,0.0075858 ,0.00756186 ,0.00757651 ,0.00749696 ,0.00757244 ,0.00736089 ,0.00758741 ,0.00773628 ,0.00702697 ,0.0087327 ,0.0103853 ,0.0106222 ,0.0111303 ,0.0112678 ,0.0148415 ,0.0169188 ,0.016911 ,0.018094]
    dn2 = [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0]
    dn1 = [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0]

    to_tev = 1e-3

    info  = "independent_variables:\n"
    info += "- header:\n"
    info += "    name: $\\tau$\n"
    info += "    units: s\n"
    info += "  values:\n"
    for lifetime in lifetimes:
        info += "  - value: {0}\n".format(lifetime)

    info += "dependent_variables:\n"
    info += "- header:\n"
    info += "    name: $\\sigma(pp \\rightarrow \\mathrm{MCHAMP} ~\\mathrm{MCHAMP}) ~\\mathcal{B}(\\mathrm{MCHAMP} \\rightarrow \\mu^{\\pm}\\mu^{\\pm})$\n"
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
    info += "    name: $\\sigma(pp \\rightarrow \\mathrm{MCHAMP} ~\\mathrm{MCHAMP}) ~\\mathcal{B}(\\mathrm{MCHAMP} \\rightarrow \\mu^{\\pm}\\mu^{\\pm})$\n"
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

    with open("lim_{0}.yaml".format(signal), "w") as f:
        f.write(info)
