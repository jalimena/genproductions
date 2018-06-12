#!/usr/bin/env python
import os, sys
import numpy as np

if __name__ == '__main__':

    ### Luminosity
    lumi = 39.0
    signal = "delayedmuon_gdecay"

    ### Gather the results
    lifetimes = ['7.5e-08', '1.0e-07', '2.0e-07', '5.0e-07', '7.0e-07', '1.0e-06', '2.0e-06', '5.0e-06', '7.0e-06', '1.0e-05', '3.0e-05', '4.0e-05', '5.0e-05', '7.0e-05', '1.0e-04', '2.0e-04', '5.0e-04', '7.0e-04', '1.0e-03', '6.0e-03', '1.0e-02', '1.0e+01', '5.0e+02', '1.0e+03', '2.0e+03', '3.6e+03', '1.0e+04', '2.0e+04', '5.0e+04', '7.0e+04', '1.0e+05', '2.0e+05', '5.0e+05', '7.0e+05', '1.0e+06']
    obs = [5.99999 ,4.48995 ,1.88671 ,0.845987 ,0.652935 ,0.571006 ,0.492063 ,0.440999 ,0.415408 ,0.415472 ,0.406603 ,0.402777 ,0.398358 ,0.398014 ,0.396068 ,0.387774 ,0.400256 ,0.390842 ,0.392697 ,0.388568 ,0.387774 ,0.389266 ,0.400056 ,0.405216 ,0.409304 ,0.435949 ,0.473196 ,0.531838 ,0.615118 ,0.637845 ,0.704358 ,0.764615 ,0.880864 ,0.926265 ,1.03273]
    exp = [5.99999 ,4.48995 ,1.88671 ,0.845987 ,0.652935 ,0.571006 ,0.492063 ,0.440999 ,0.415408 ,0.415472 ,0.406603 ,0.402777 ,0.398358 ,0.398014 ,0.396068 ,0.387774 ,0.400256 ,0.390842 ,0.392697 ,0.388568 ,0.387774 ,0.389266 ,0.400056 ,0.405216 ,0.409304 ,0.435949 ,0.473196 ,0.531838 ,0.615118 ,0.637845 ,0.704358 ,0.764615 ,0.880864 ,0.926265 ,1.03273]
    up2 = [7.92591 ,1.51005 ,1.04517 ,0.836373 ,0.658094 ,0.549405 ,0.594997 ,0.610862 ,0.596162 ,0.574019 ,0.556241 ,0.567615 ,0.574783 ,0.573802 ,0.575747 ,0.585367 ,0.572461 ,0.581326 ,0.579167 ,0.583246 ,0.584508 ,0.583079 ,0.571556 ,0.558942 ,0.568164 ,0.590812 ,0.676644 ,0.753392 ,0.872653 ,0.941074 ,0.982162 ,1.07336 ,1.32236 ,1.37415 ,1.41403]
    up1 = [0 ,0 ,0 ,0.444362 ,0.318148 ,0.270358 ,0.215143 ,0.188771 ,0.189675 ,0.187965 ,0.17688 ,0.18015 ,0.184208 ,0.192205 ,0.191681 ,0.191284 ,0.18717 ,0.188278 ,0.190868 ,0.198286 ,0.191284 ,0.194572 ,0.184403 ,0.184914 ,0.191193 ,0.190688 ,0.227294 ,0.235026 ,0.255568 ,0.294816 ,0.296733 ,0.347926 ,0.431036 ,0.447835 ,0.461059]
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

    #print info.rstrip("\n")

    with open("lim_{0}.yaml".format(signal), "w") as f:
        f.write(info)
