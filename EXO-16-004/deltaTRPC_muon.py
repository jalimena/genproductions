#!/usr/bin/env python
import os, sys
import numpy as np

if __name__ == '__main__':

    lumi = 36.2

    deltaTRPC = [-105, -100, -95, -90, -85, -80, -75, -70, -65, -60, -55, -50, -45, -40, -35, -30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105]

    data = [
0.0002625413,
0.0002625413,
0,
0,
0,
0,
6.152194e-05,
0.0001106441,
0.001027035,
0.01173114,
0.01466702,
0.1131501,
0.1522456,
0.1795298,
0.2489812,
0.1395041,
0.126697,
0.009647975,
0.001612447,
0.0002592029,
1.83612e-05,
3.600703e-05,
1.192286e-06,
2.384571e-06,
4.769143e-07,
0,
9.538285e-07,
0,
1.192286e-06,
7.153714e-07,
0,
9.538285e-07,
4.769143e-07,
0,
0,
0,
2.861486e-06,
0,
0,
0,
0.0004471071,
0.0004471071
        ]
    error_data = [
7.912322e-06,
7.912322e-06,
0,
0,
0,
0,
3.830189e-06,
5.136524e-06,
1.56494e-05,
5.28902e-05,
5.913929e-05,
0.0001642603,
0.0001905362,
0.0002069062,
0.0002436623,
0.000182389,
0.0001738155,
4.796487e-05,
1.960866e-05,
7.861856e-06,
2.092453e-06,
2.93021e-06,
5.332063e-07,
7.540676e-07,
3.372293e-07,
0,
4.769143e-07,
0,
5.332063e-07,
4.130199e-07,
0,
4.769143e-07,
3.372293e-07,
0,
0,
0,
8.260397e-07,
0,
0,
0,
1.03255e-05,
1.03255e-05
        ]

    cosmicMC = [
0,
3.147128e-05,
0,
0,
0,
0,
0,
3.147128e-05,
0.001605035,
0.01740362,
0.01063729,
0.1850197,
0.158867,
0.1472856,
0.2053816,
0.1147128,
0.1546499,
0.003587726,
0.0005979544,
9.441385e-05,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
9.441385e-05,
9.441385e-05
        ]
    error_cosmicMC = [
0,
3.147128e-05,
0,
0,
0,
0,
0,
3.147128e-05,
0.0002247499,
0.0007400772,
0.0005785925,
0.002413049,
0.002236012,
0.002152967,
0.002542365,
0.001900042,
0.002206135,
0.0003360213,
0.0001371801,
5.450986e-05,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
5.450986e-05,
5.450986e-05
        ]

    gluinos = [
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0.004651163,
0.009302326,
0,
0,
0,
0,
0,
0,
0.9627907,
0.004651163,
0.009302326,
0,
0,
0.009302326,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0
        ]
    error_gluinos = [
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0.004651163,
0.006577737,
0,
0,
0,
0,
0,
0,
0.06691858,
0.004651163,
0.006577737,
0,
0,
0.006577737,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0
        ]
    
    mchamps = [
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0.004504505,
0.002252252,
0.002252252,
0,
0,
0,
0.004504505,
0.006756757,
0.004504505,
0.9572072,
0.006756757,
0.002252252,
0.002252252,
0,
0,
0,
0.002252252,
0.002252252,
0,
0.002252252,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0
        ]
    error_mchamps = [
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0.003185166,
0.002252252,
0.002252252,
0,
0,
0,
0.003185166,
0.003901015,
0.003185166,
0.04643137,
0.003901015,
0.002252252,
0.002252252,
0,
0,
0,
0.002252252,
0.002252252,
0,
0.002252252,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0
        ]

    info  = "independent_variables:\n"
    info += "- header:\n"
    info += "    name: $\\Delta t_{\\mathrm{RPC}}$\n"
    info += "    units: ns\n"
    info += "  values:\n"
    for v in range(len(deltaTRPC)-1):
        high = deltaTRPC[v+1]
        low = deltaTRPC[v]
        info += "  - {{high: {0}, low: {1}}}\n".format(high,low)

    info += "dependent_variables:\n"

    info += "- header:\n"
    info += "    name: Fraction of Entries / 5.0 ns\n"
    info += "  qualifiers:\n"
    info += "  - {name: Sample, value: Data}\n"
    info += "  - {{name: LUMINOSITY, units: 'fb$^{{-1}}$', value: {0}}}\n".format(lumi)
    info += "  values:\n"
    for idx in range(len(deltaTRPC)-1):
        v = data[idx]
        v_e = error_data[idx]
        info += "  - value: {0:.6g}\n".format(v)
        info += "    errors:\n"
        info += "    - {{symerror: {0:.6g}, label: 'stat'}}\n".format(v_e)

    info += "- header:\n"
    info += "    name: Fraction of Entries / 5.0 ns\n"
    info += "  qualifiers:\n"
    info += "  - {name: Sample, value: Cosmic ray muon simulation}\n"
    info += "  - {{name: LUMINOSITY, units: 'fb$^{{-1}}$', value: {0}}}\n".format(lumi)
    info += "  values:\n"
    for idx in range(len(deltaTRPC)-1):
        v = cosmicMC[idx]
        v_e = error_cosmicMC[idx]
        info += "  - value: {0:.6g}\n".format(v)
        info += "    errors:\n"
        info += "    - {{symerror: {0:.6g}, label: 'stat'}}\n".format(v_e)

    info += "- header:\n"
    info += "    name: Fraction of Entries / 5.0 ns\n"
    info += "  qualifiers:\n"
    info += "  - {name: Sample, value: '$\\tilde{g} \\rightarrow q\\bar{q}\\tilde{\\chi}^{0}_{2}$, $\\tilde{\\chi}^{0}_{2} \\rightarrow \\mu^{+}\\mu^{-}\\tilde{\\chi}^{0}$ ($m_{\\tilde{g}}$ = 1000 GeV, $m_{\\tilde{\\chi}^{0}_{2}}$ = 625 GeV, $m_{\\tilde{\\chi}^{0}}$ = 250 GeV)'}\n"
    info += "  - {{name: LUMINOSITY, units: 'fb$^{{-1}}$', value: {0}}}\n".format(lumi)
    info += "  values:\n"
    for idx in range(len(deltaTRPC)-1):
        v = gluinos[idx]
        v_e = error_gluinos[idx]
        info += "  - value: {0:.6g}\n".format(v)
        info += "    errors:\n"
        info += "    - {{symerror: {0:.6g}, label: 'stat'}}\n".format(v_e)

    info += "- header:\n"
    info += "    name: Fraction of Entries / 5.0 ns\n"
    info += "  qualifiers:\n"
    info += "  - {name: Sample, value: '$\\mathrm{MCHAMP} \\rightarrow \\mu^{\\pm}\\mu^{\\pm}$ (|Q| = 2e, $m_{\\mathrm{MCHAMP}}$ = 600 GeV)'}\n"
    info += "  - {{name: LUMINOSITY, units: 'fb$^{{-1}}$', value: {0}}}\n".format(lumi)
    info += "  values:\n"
    for idx in range(len(deltaTRPC)-1):
        v = mchamps[idx]
        v_e = error_mchamps[idx]
        info += "  - value: {0:.6g}\n".format(v)
        info += "    errors:\n"
        info += "    - {{symerror: {0:.6g}, label: 'stat'}}\n".format(v_e)

    with open("deltaTRPC.yaml", "w") as f:
        f.write(info)
