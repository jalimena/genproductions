#!/usr/bin/env python
import os, sys
import numpy as np

if __name__ == '__main__':

    ### Luminosity
    lumi = 38.6
    signal = "g3bdecay"

    ### Gather the results
    lifetimes = ['7.5e-08', '1.0e-07', '1.39058e-07', '1.58923e-07', '2.0e-07', '2.78116e-07', '2.97981e-07', '4.96636e-07', '5.0e-07', '5.16501e-07', '5.36366e-07', '5.56232e-07', '5.76097e-07', '6.15828e-07', '6.35694e-07', '7.0e-07', '1.0e-06', '1.43031e-06', '1.45018e-06', '1.62896e-06', '1.64883e-06', '1.96668e-06', '1.98654e-06', '2.0e-06', '3.43672e-06', '3.45658e-06', '4.46972e-06', '4.48959e-06', '4.50945e-06', '5.0e-06', '7.0e-06', '1.0e-05', '1.05883e-05', '1.06081e-05', '3.0e-05', '4.0e-05', '5.0e-05', '7.0e-05', '1.0e-04', '2.0e-04', '5.0e-04', '7.0e-04', '1.0e-03', '6.0e-03', '1.0e-02', '1.0e+01', '5.0e+02', '1.0e+03', '2.0e+03', '3.6e+03', '1.0e+04', '2.0e+04', '5.0e+04', '7.0e+04', '1.0e+05', '2.0e+05', '5.0e+05', '7.0e+05', '1.0e+06']
    obs = [0.174999 ,0.0880383 ,0.0543381 ,0.0488109 ,0.0426298 ,0.0307035 ,0.0292572 ,0.0170137 ,0.0170137 ,0.023573 ,0.0230735 ,0.0246372 ,0.0242602 ,0.028087 ,0.0347018 ,0.0320628 ,0.0266204 ,0.0233793 ,0.0259174 ,0.0249323 ,0.0251013 ,0.0253316 ,0.0261758 ,0.0281881 ,0.0260716 ,0.025287 ,0.0264622 ,0.0302053 ,0.0293673 ,0.0284567 ,0.0275267 ,0.0270197 ,0.0264925 ,0.0264925 ,0.0266234 ,0.0266233 ,0.0266233 ,0.0261587 ,0.0261587 ,0.0266233 ,0.0261587 ,0.0266234 ,0.0261587 ,0.0261587 ,0.0266233 ,0.0261587 ,0.0266233 ,0.02641 ,0.027075 ,0.0276989 ,0.0308578 ,0.0344879 ,0.0398812 ,0.041555 ,0.0440584 ,0.0475487 ,0.0586181 ,0.0625567 ,0.0665925]
    exp = [0.233131 ,0.141246 ,0.10294 ,0.0962346 ,0.0799369 ,0.0669768 ,0.0649038 ,0.0559939 ,0.052124 ,0.0519192 ,0.0512648 ,0.0503642 ,0.0500743 ,0.0495443 ,0.0496051 ,0.0474842 ,0.0446885 ,0.0418577 ,0.0431881 ,0.0417888 ,0.0415903 ,0.0408181 ,0.0399742 ,0.0406327 ,0.0401075 ,0.0399073 ,0.0401066 ,0.0409298 ,0.0411941 ,0.0390392 ,0.0399841 ,0.0403414 ,0.0397262 ,0.0397262 ,0.039301 ,0.039301 ,0.039301 ,0.0400525 ,0.0400525 ,0.039301 ,0.0400526 ,0.039301 ,0.0400525 ,0.0400525 ,0.039301 ,0.0400525 ,0.039301 ,0.0399269 ,0.0411765 ,0.0425714 ,0.0465179 ,0.0516027 ,0.0594459 ,0.062899 ,0.0666516 ,0.0733864 ,0.0871247 ,0.0930893 ,0.0989655]
    up2 = [0.26884 ,0.194246 ,0.142331 ,0.124155 ,0.116356 ,0.104641 ,0.096807 ,0.0849632 ,0.0886782 ,0.0885024 ,0.0886644 ,0.0913521 ,0.0894013 ,0.0898095 ,0.0875569 ,0.0938446 ,0.0861751 ,0.0857762 ,0.0801101 ,0.0805744 ,0.0756922 ,0.0839138 ,0.0864938 ,0.0863228 ,0.0843856 ,0.0844979 ,0.0837312 ,0.0785254 ,0.0811382 ,0.0857486 ,0.0836718 ,0.0863164 ,0.0850186 ,0.0850186 ,0.0846087 ,0.0846087 ,0.0846087 ,0.0826084 ,0.0826084 ,0.0846087 ,0.0826084 ,0.0846086 ,0.0826084 ,0.0826084 ,0.0846086 ,0.0826084 ,0.0846086 ,0.0827581 ,0.0862875 ,0.081516 ,0.0992043 ,0.108821 ,0.131196 ,0.135792 ,0.146113 ,0.161956 ,0.18607 ,0.198495 ,0.197754]
    up1 = [0.139821 ,0.0771408 ,0.0509917 ,0.0529271 ,0.0494222 ,0.0374418 ,0.0387436 ,0.0314934 ,0.0351929 ,0.0353266 ,0.0310647 ,0.0338955 ,0.0330096 ,0.0324302 ,0.0347525 ,0.034301 ,0.0321613 ,0.0317594 ,0.0312099 ,0.0315975 ,0.0310229 ,0.0311639 ,0.0322216 ,0.0315963 ,0.032237 ,0.0316802 ,0.0324243 ,0.0310437 ,0.0307372 ,0.0322406 ,0.0330968 ,0.0316774 ,0.033464 ,0.033464 ,0.0330781 ,0.0330781 ,0.0330781 ,0.0312931 ,0.0312931 ,0.0330781 ,0.0312931 ,0.0330781 ,0.0312931 ,0.0312931 ,0.0330781 ,0.0312931 ,0.0330781 ,0.0322879 ,0.0315978 ,0.0319886 ,0.0375509 ,0.0394895 ,0.0502583 ,0.0491479 ,0.0531972 ,0.0623891 ,0.0687891 ,0.0722318 ,0.0770886]
    dn2 = [0.0576572 ,0.0506571 ,0.0404904 ,0.0421713 ,0.0357122 ,0.0335677 ,0.0315431 ,0.0318613 ,0.0278523 ,0.0277974 ,0.0232438 ,0.027047 ,0.0271563 ,0.0271222 ,0.0280644 ,0.0301582 ,0.0252893 ,0.0246418 ,0.0272798 ,0.0244582 ,0.0242584 ,0.0238727 ,0.0232286 ,0.0234642 ,0.0232447 ,0.0235734 ,0.0234556 ,0.0245052 ,0.0249877 ,0.0227624 ,0.0244682 ,0.0241308 ,0.0234821 ,0.0234821 ,0.0237549 ,0.0237549 ,0.0237549 ,0.0242535 ,0.0242535 ,0.0237549 ,0.0242535 ,0.0237549 ,0.0242535 ,0.0242535 ,0.0237549 ,0.0242535 ,0.0237549 ,0.0241277 ,0.0247793 ,0.0261314 ,0.0281936 ,0.0312813 ,0.0362607 ,0.0372211 ,0.0404614 ,0.0442216 ,0.0521887 ,0.0563264 ,0.060115]
    dn1 = [0.0576572 ,0.0221151 ,0.0287162 ,0.0228079 ,0.0266949 ,0.0229068 ,0.0210904 ,0.0226801 ,0.0180594 ,0.0185868 ,0.0190555 ,0.0185141 ,0.0186324 ,0.0187251 ,0.0188158 ,0.0183042 ,0.0175419 ,0.0158814 ,0.0173282 ,0.0165582 ,0.0161046 ,0.0164125 ,0.0136263 ,0.0157673 ,0.0154311 ,0.0152768 ,0.0154481 ,0.0157661 ,0.0164939 ,0.0148037 ,0.0158286 ,0.0163957 ,0.0152144 ,0.0152143 ,0.0158473 ,0.0158473 ,0.0158473 ,0.0161794 ,0.0161794 ,0.0158473 ,0.0161794 ,0.0158473 ,0.0161794 ,0.0161794 ,0.0158473 ,0.0161794 ,0.0158473 ,0.0157107 ,0.0166987 ,0.0175897 ,0.017658 ,0.0209948 ,0.0239625 ,0.0255662 ,0.0266358 ,0.0290062 ,0.0354791 ,0.0388376 ,0.0406572]

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
    info += "    name: $\\sigma(pp \\rightarrow \\tilde{g}\\tilde{g}) ~\\mathcal{B}(\\tilde{g} \\rightarrow q\\bar{q}\\tilde{\\chi}^{0})$\n"
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
    info += "    name: $\\sigma(pp \\rightarrow \\tilde{g}\\tilde{g}) ~\\mathcal{B}(\\tilde{g} \\rightarrow q\\bar{q}\\tilde{\\chi}^{0})$\n"
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
