#!/usr/bin/env python
import os, sys
import numpy as np

if __name__ == '__main__':

    ### Luminosity
    lumi = 38.6
    signal = "g2bdecaymass"

    ### Gather the results
    lifetimes = ['7.5e-08', '1.0e-07', '1.39058e-07', '1.58923e-07', '2.0e-07', '2.78116e-07', '2.97981e-07', '4.96636e-07', '5.0e-07', '5.16501e-07', '5.36366e-07', '5.56232e-07', '5.76097e-07', '6.15828e-07', '6.35694e-07', '7.0e-07', '1.0e-06', '1.43031e-06', '1.45018e-06', '1.62896e-06', '1.64883e-06', '1.96668e-06', '1.98654e-06', '2.0e-06', '3.43672e-06', '3.45658e-06', '4.46972e-06', '4.48959e-06', '4.50945e-06', '5.0e-06', '7.0e-06', '1.0e-05', '1.05883e-05', '1.06081e-05', '3.0e-05', '4.0e-05', '5.0e-05', '7.0e-05', '1.0e-04', '2.0e-04', '5.0e-04', '7.0e-04', '1.0e-03', '6.0e-03', '1.0e-02', '1.0e+01', '5.0e+02', '1.0e+03', '2.0e+03', '3.6e+03', '1.0e+04', '2.0e+04', '5.0e+04', '7.0e+04', '1.0e+05', '2.0e+05', '5.0e+05', '7.0e+05', '1.0e+06']
    obs = [1080.5 ,1186.04 ,1263.17 ,1280.49 ,1302.66 ,1360.31 ,1367.48 ,1457.62 ,1457.62 ,1399.59 ,1403.33 ,1393.02 ,1395.32 ,1373.55 ,1340.3 ,1353.88 ,1381.52 ,1400.98 ,1385.5 ,1391.26 ,1390.25 ,1388.89 ,1384.02 ,1373.02 ,1384.62 ,1389.16 ,1382.41 ,1362.75 ,1366.93 ,1371.61 ,1376.54 ,1379.31 ,1382.24 ,1382.24 ,1381.5 ,1381.5 ,1381.5 ,1384.12 ,1384.12 ,1381.5 ,1384.12 ,1381.5 ,1384.12 ,1384.12 ,1381.5 ,1384.12 ,1381.5 ,1382.7 ,1379 ,1375.62 ,1359.57 ,1341.43 ,1314.85 ,1307.33 ,1297.02 ,1284.72 ,1250.93 ,1240.48 ,1230.44]
    exp = [1038.66 ,1112.64 ,1161.68 ,1172.17 ,1201.11 ,1229.52 ,1234.57 ,1258.32 ,1269.89 ,1270.52 ,1272.57 ,1275.43 ,1276.36 ,1278.08 ,1277.88 ,1284.94 ,1294.73 ,1306 ,1300.28 ,1306.3 ,1307.17 ,1310.6 ,1314.43 ,1311.44 ,1313.82 ,1314.73 ,1313.82 ,1310.1 ,1308.93 ,1318.76 ,1314.38 ,1312.75 ,1315.56 ,1315.56 ,1317.53 ,1317.53 ,1317.53 ,1314.07 ,1314.07 ,1317.53 ,1314.07 ,1317.53 ,1314.07 ,1314.07 ,1317.53 ,1314.07 ,1317.53 ,1314.64 ,1309 ,1302.91 ,1288.25 ,1271.51 ,1248.67 ,1239.6 ,1230.3 ,1214.84 ,1187.66 ,1177.35 ,1167.81]
    up2 = [41.4465 ,68.9454 ,79.0769 ,91.8172 ,95.3096 ,117.733 ,112.948 ,137.776 ,125.36 ,125.645 ,101.332 ,126.023 ,128.177 ,130.371 ,137.737 ,169.505 ,139.605 ,149.553 ,169.091 ,148.091 ,147.207 ,147.722 ,145.974 ,144.601 ,145.364 ,150.02 ,147.569 ,153.681 ,157.197 ,146.609 ,159.356 ,153.325 ,150.152 ,150.152 ,155.864 ,155.864 ,155.864 ,156.507 ,156.507 ,155.864 ,156.507 ,155.864 ,156.507 ,156.507 ,155.864 ,156.507 ,155.864 ,155.931 ,155.073 ,160.711 ,156.271 ,154.526 ,153.795 ,147.272 ,153.643 ,153.117 ,151.411 ,152.4 ,151.83]
    up1 = [41.4465 ,26.3539 ,51.3366 ,42.5788 ,65.3528 ,67.4657 ,63.359 ,89.4476 ,73.8082 ,77.1483 ,80.6314 ,79.4369 ,80.4217 ,81.6766 ,82.0183 ,82.9418 ,83.8793 ,79.1573 ,85.5493 ,83.1841 ,80.8181 ,83.8249 ,68.6231 ,80.2181 ,78.9716 ,78.333 ,79.0758 ,79.7789 ,83.719 ,76.7117 ,81.5787 ,84.5021 ,78.2186 ,78.2184 ,82.8762 ,82.8762 ,82.8763 ,83.6385 ,83.6385 ,82.8762 ,83.6385 ,82.8763 ,83.6385 ,83.6385 ,82.8764 ,83.6384 ,82.8762 ,80.9439 ,84.9854 ,88.0522 ,81.262 ,89.2705 ,87.5551 ,87.3285 ,83.9377 ,81.0114 ,83.7123 ,86.0796 ,83.973]
    dn2 = [106.851 ,125.593 ,130.273 ,125.489 ,137.494 ,146.146 ,142.451 ,145.364 ,156.755 ,156.972 ,158.476 ,163.302 ,161.767 ,163.349 ,160.698 ,172.384 ,170.273 ,177.676 ,166.603 ,171.45 ,165.758 ,178.718 ,184.679 ,182.285 ,181.634 ,182.44 ,180.821 ,171.528 ,174.034 ,186.939 ,181.153 ,183.238 ,183.694 ,183.694 ,184.623 ,184.623 ,184.623 ,179.59 ,179.59 ,184.623 ,179.59 ,184.623 ,179.59 ,179.59 ,184.623 ,179.59 ,184.623 ,180.196 ,180.472 ,170.221 ,180.441 ,178.219 ,180.765 ,177.778 ,178.536 ,177.531 ,171.654 ,170.644 ,163.602]
    dn1 = [66.292 ,64.6572 ,62.314 ,67.9674 ,74.858 ,70.0582 ,73.9531 ,71.3092 ,82.567 ,83.0757 ,76.0892 ,82.5601 ,81.3032 ,80.927 ,85.1927 ,87.4233 ,87.3002 ,91.6683 ,87.6385 ,91.4652 ,90.6358 ,92.6623 ,96.9607 ,94.0453 ,96.6821 ,95.9082 ,97.0995 ,92.1432 ,90.8716 ,99.2402 ,98.8724 ,94.8936 ,100.296 ,100.296 ,100.475 ,100.475 ,100.475 ,94.7002 ,94.7002 ,100.475 ,94.7001 ,100.475 ,94.7002 ,94.7002 ,100.475 ,94.7002 ,100.475 ,97.2197 ,92.8211 ,90.6191 ,95.0319 ,90.783 ,96.9067 ,91.1199 ,92.231 ,96.0819 ,90.1781 ,88.4799 ,88.1963]

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
    info += "    name: $\\textrm{m}_{\\tilde{g}}$\n"
    info += "    units: GeV\n"
    info += "  qualifiers:\n"
    info += "  - {name: Limit, value: Observed}\n"
    #info += "  - {name: SQRT(S), units: GeV, value: 13000}\n"
    info += "  - {{name: LUMINOSITY, units: 'fb$^{{-1}}$', value: {0}}}\n".format(lumi)
    info += "  values:\n"

    for idx in range( len(obs) ):
        lim = obs[idx]
        info += "  - value: {0:.6g}\n".format(lim)

    info += "- header:\n"
    info += "    name: $\\textrm{m}_{\\tilde{g}}$\n"
    info += "    units: GeV\n"
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
