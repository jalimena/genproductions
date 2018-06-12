#!/usr/bin/env python
import os, sys
import numpy as np

if __name__ == '__main__':

    cut_delta_tRPC2016 = [-100, -50, -45, -40, -35, -30, -25, -20, -15, -10]
    int_delta_tDT2016 = [414,394,380,340,293,163,37.5,17.8,3.88,0.51]
    errorPlus_int_delta_tDT2016 = [66,33,28,22,48,63,1.9,7.8,1.88,0.23]
    errorMinus_int_delta_tDT2016 = [66,33,28,22,31,63,1.9,7.8,1.88,0.23]

    cut_delta_tRPC2015 = [-100, -50, -45, -40, -35, -30, -25, -15, -10]
    int_delta_tDT2015 = [43.6,38.3,36.7,32.9,27,13.7,2.11,1.59,0.04]
    errorPlus_int_delta_tDT2015 = [4.7,11.3,6.8,11.5,0.9,6.6,1.02,0.59,0.03]
    errorMinus_int_delta_tDT2015 = [4.9,11.2,10.7,3.0,17,6.6,1.02,1.59,0]

    info  = "independent_variables:\n"
    info += "- header:\n"
    info += "    name: Lower $\\Delta t_{\\mathrm{RPC}}$ threshold\n"
    info += "    units: ns\n"
    info += "  values:\n"
    for v in cut_delta_tRPC2016:
        info += "  - value: {0}\n".format(v)

    info += "dependent_variables:\n"

    info += "- header:\n"
    info += "    name: Fit integral for $\\Delta t_{\\mathrm{DT}}$ > -20 ns\n"
    info += "  qualifiers:\n"
    info += "  - {name: Year, value: 2015}\n"
    info += "  values:\n"
    for idx in range(len(cut_delta_tRPC2015)):
        v = int_delta_tDT2015[idx]
        if cut_delta_tRPC2015[idx] == -15:
            info += "  - value: ' '\n"
        v_up1 = errorPlus_int_delta_tDT2015[idx]
        v_dn1 = errorMinus_int_delta_tDT2015[idx]
        info += "  - value: {0:.6g}\n".format(v)
        info += "    errors:\n"
        info += "    - {{asymerror: {{plus: {0:.6g}, minus: {1:.6g}}}, label: 'stat'}}\n".format(v_up1, -v_dn1)

    info += "- header:\n"
    info += "    name: Fit integral for $\\Delta t_{\\mathrm{DT}}$ > -20 ns\n"
    info += "  qualifiers:\n"
    info += "  - {name: Year, value: 2016}\n"
    info += "  values:\n"
    for idx in range(len(cut_delta_tRPC2016)):
        v = int_delta_tDT2016[idx]
        v_up1 = errorPlus_int_delta_tDT2016[idx]
        v_dn1 = errorMinus_int_delta_tDT2016[idx]
        info += "  - value: {0:.6g}\n".format(v)
        info += "    errors:\n"
        info += "    - {{asymerror: {{plus: {0:.6g}, minus: {1:.6g}}}, label: 'stat'}}\n".format(v_up1, -v_dn1)

    with open("background_extrapolating.yaml", "w") as f:
        f.write(info)
