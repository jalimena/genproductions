#!/usr/bin/env python
import os, sys
import numpy as np

if __name__ == '__main__':

    ### Luminosity
    lumi = 38.6
    signal = "g2bdecay"

    ### Gather the results
    lifetimes = ['7.5e-08', '1.0e-07', '1.39058e-07', '1.58923e-07', '2.0e-07', '2.78116e-07', '2.97981e-07', '4.96636e-07', '5.0e-07', '5.16501e-07', '5.36366e-07', '5.56232e-07', '5.76097e-07', '6.15828e-07', '6.35694e-07', '7.0e-07', '1.0e-06', '1.43031e-06', '1.45018e-06', '1.62896e-06', '1.64883e-06', '1.96668e-06', '1.98654e-06', '2.0e-06', '3.43672e-06', '3.45658e-06', '4.46972e-06', '4.48959e-06', '4.50945e-06', '5.0e-06', '7.0e-06', '1.0e-05', '1.05883e-05', '1.06081e-05', '3.0e-05', '4.0e-05', '5.0e-05', '7.0e-05', '1.0e-04', '2.0e-04', '5.0e-04', '7.0e-04', '1.0e-03', '6.0e-03', '1.0e-02', '1.0e+01', '5.0e+02', '1.0e+03', '2.0e+03', '3.6e+03', '1.0e+04', '2.0e+04', '5.0e+04', '7.0e+04', '1.0e+05', '2.0e+05', '5.0e+05', '7.0e+05', '1.0e+06']
    obs = [0.18611 ,0.093628 ,0.0577881 ,0.05191 ,0.0453365 ,0.0326529 ,0.0311148 ,0.0180939 ,0.0180939 ,0.0250697 ,0.0245385 ,0.0262014 ,0.0258005 ,0.0298703 ,0.0369051 ,0.0340985 ,0.0283106 ,0.0248637 ,0.0275629 ,0.0265153 ,0.026695 ,0.0269399 ,0.0278378 ,0.0299779 ,0.0277269 ,0.0268925 ,0.0281424 ,0.0321231 ,0.0312319 ,0.0302634 ,0.0292744 ,0.0287353 ,0.0281745 ,0.0281745 ,0.0283137 ,0.0283137 ,0.0283137 ,0.0278196 ,0.0278196 ,0.0283137 ,0.0278196 ,0.0283137 ,0.0278196 ,0.0278196 ,0.0283137 ,0.0278196 ,0.0283137 ,0.0280868 ,0.028794 ,0.0294576 ,0.032817 ,0.0366777 ,0.0424133 ,0.0441934 ,0.0468558 ,0.0505677 ,0.0623398 ,0.0665286 ,0.0708206 ]
    exp = [0.247933 ,0.150214 ,0.109476 ,0.102345 ,0.0850123 ,0.0712293 ,0.0690247 ,0.0595491 ,0.0554335 ,0.0552157 ,0.0545197 ,0.0535619 ,0.0532537 ,0.05269 ,0.0527547 ,0.0504991 ,0.0475258 ,0.0445153 ,0.0459302 ,0.0444421 ,0.0442309 ,0.0434097 ,0.0425123 ,0.0432126 ,0.042654 ,0.0424411 ,0.042653 ,0.0435286 ,0.0438096 ,0.0415179 ,0.0425228 ,0.0429028 ,0.0422485 ,0.0422485 ,0.0417963 ,0.0417963 ,0.0417963 ,0.0425955 ,0.0425956 ,0.0417963 ,0.0425956 ,0.0417963 ,0.0425956 ,0.0425955 ,0.0417963 ,0.0425956 ,0.0417963 ,0.0424619 ,0.0437909 ,0.0452744 ,0.0494714 ,0.054879 ,0.0632203 ,0.0668926 ,0.0708834 ,0.0780458 ,0.0926564 ,0.0989997 ,0.105249 ]
    up2 = [0.285909 ,0.20658 ,0.151368 ,0.132038 ,0.123744 ,0.111285 ,0.102953 ,0.0903577 ,0.0943086 ,0.0941216 ,0.0942938 ,0.0971523 ,0.0950776 ,0.0955117 ,0.0931161 ,0.0998029 ,0.0916465 ,0.0912223 ,0.0851965 ,0.0856902 ,0.0804981 ,0.0892416 ,0.0919855 ,0.0918036 ,0.0897434 ,0.0898628 ,0.0890474 ,0.0835111 ,0.0862898 ,0.0911929 ,0.0889843 ,0.0917968 ,0.0904166 ,0.0904167 ,0.0899806 ,0.0899806 ,0.0899806 ,0.0878534 ,0.0878534 ,0.0899806 ,0.0878534 ,0.0899806 ,0.0878534 ,0.0878534 ,0.0899806 ,0.0878534 ,0.0899806 ,0.0880125 ,0.0917661 ,0.0866916 ,0.105503 ,0.115731 ,0.139526 ,0.144414 ,0.15539 ,0.172239 ,0.197883 ,0.211098 ,0.210309]
    up1 = [0.148699 ,0.0820387 ,0.0542292 ,0.0562876 ,0.0525601 ,0.0398191 ,0.0412036 ,0.033493 ,0.0374273 ,0.0375695 ,0.033037 ,0.0360476 ,0.0351055 ,0.0344892 ,0.036959 ,0.0364789 ,0.0342033 ,0.0337758 ,0.0331915 ,0.0336036 ,0.0329926 ,0.0331425 ,0.0342674 ,0.0336024 ,0.0342838 ,0.0336916 ,0.034483 ,0.0330147 ,0.0326888 ,0.0342876 ,0.0351982 ,0.0336887 ,0.0355887 ,0.0355887 ,0.0351783 ,0.0351783 ,0.0351783 ,0.03328 ,0.03328 ,0.0351783 ,0.03328 ,0.0351783 ,0.03328 ,0.03328 ,0.0351783 ,0.03328 ,0.0351783 ,0.0343379 ,0.033604 ,0.0340197 ,0.0399351 ,0.0419968 ,0.0534493 ,0.0522684 ,0.0565748 ,0.0663503 ,0.0731567 ,0.0768179 ,0.0819831]
    dn2 = [0.061318 ,0.0538735 ,0.0430612 ,0.0448489 ,0.0379797 ,0.035699 ,0.0335458 ,0.0338842 ,0.0296207 ,0.0295623 ,0.0247196 ,0.0287643 ,0.0288805 ,0.0288443 ,0.0298463 ,0.032073 ,0.026895 ,0.0262063 ,0.0290118 ,0.0260111 ,0.0257986 ,0.0253884 ,0.0247035 ,0.024954 ,0.0247206 ,0.0250701 ,0.0249448 ,0.0260611 ,0.0265742 ,0.0242076 ,0.0260217 ,0.0256629 ,0.024973 ,0.024973 ,0.0252631 ,0.0252631 ,0.0252631 ,0.0257934 ,0.0257934 ,0.0252631 ,0.0257934 ,0.0252632 ,0.0257934 ,0.0257934 ,0.0252631 ,0.0257934 ,0.0252631 ,0.0256596 ,0.0263526 ,0.0277906 ,0.0299837 ,0.0332674 ,0.038563 ,0.0395843 ,0.0430304 ,0.0470293 ,0.0555022 ,0.0599027 ,0.0639318]
    dn1 = [0.061318 ,0.0235192 ,0.0305395 ,0.024256 ,0.0283898 ,0.0243612 ,0.0224295 ,0.0241201 ,0.019206 ,0.0197669 ,0.0202654 ,0.0196896 ,0.0198154 ,0.019914 ,0.0200104 ,0.0194664 ,0.0186556 ,0.0168897 ,0.0184284 ,0.0176095 ,0.0171271 ,0.0174546 ,0.0144914 ,0.0167684 ,0.0164108 ,0.0162467 ,0.016429 ,0.0167671 ,0.0175411 ,0.0157436 ,0.0168336 ,0.0174367 ,0.0161804 ,0.0161803 ,0.0168535 ,0.0168535 ,0.0168535 ,0.0172066 ,0.0172066 ,0.0168535 ,0.0172067 ,0.0168535 ,0.0172066 ,0.0172066 ,0.0168535 ,0.0172066 ,0.0168535 ,0.0167082 ,0.017759 ,0.0187065 ,0.0187792 ,0.0223279 ,0.0254839 ,0.0271895 ,0.028327 ,0.0308478 ,0.0377317 ,0.0413035 ,0.0432386]

    to_tev = 1e-3

    info  = "independent_variables:\n"
    info += "- header:\n"
    info += "    name: $\\tau$\n"
    info += "    units: s\n"
    info += "  values:\n"
    for lifetime in lifetimes:
        info += "  - value: {0}\n".format(str(lifetime))

    info += "dependent_variables:\n"
    info += "- header:\n"
    info += "    name: $\\sigma(pp \\rightarrow \\tilde{g}\\tilde{g}) ~\\mathcal{B}(\\tilde{g} \\rightarrow g\\tilde{\\chi}^{0})$\n"
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
    info += "    name: $\\sigma(pp \\rightarrow \\tilde{g}\\tilde{g}) ~\\mathcal{B}(\\tilde{g} \\rightarrow g\\tilde{\\chi}^{0})$\n"
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
