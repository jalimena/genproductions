#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import numpy as np
from hepdata_lib import *


def make_table_4(outdir):
    # This is the raw data from EXO-16-052
    # Table 4
    # It has four columns, corresponding to four variables
    data = [
        [(100, 125), 311, (300,    18), (256, 32)],
        [(125, 150), 155, (155.0, 7.0), (150, 12)],
        [(150, 175), 87, (90.8, 4.6), (86.9, 8.4)],
        [(175, 200), 50, (54.7, 3.1), (52.7, 5.3)],
        [(200, 250), 56, (51.3, 2.9), (50.2, 4.9)],
        [(250, 300), 15, (19.7, 1.4), (19.4, 2.2)],
        [(300, 350), 11, (9.64, 0.80), (9.4, 1.2)],
        [(350, 400), 6, (4.73, 0.47), (4.58, 0.66)],
        [(400, 500), 6, (3.44, 0.39), (3.31, 0.54)],
        [(500, 600), 1, (1.63, 0.24), (1.57, 0.33)]
    ]

    table = Table("Event yields in the signal region")
    table.location = "Table 4, located on page 17."
    table.description = """Expected event yields in each $p_{\mathrm{T}}^{\mathrm{miss}}$ bin for the sum of background processes in the signal region (SR).
The background yields and their corresponding uncertainties are obtained after performing a fit to data.
Two sets of background yields are reported: one from a background-only fit to data in both the SR and the control regions (CRs), and one from a fit to data in all CRs, but excluding data in the SR.
The observed numbers of events in each bin are also included. The last bin includes overflow."""

    # First variable/column ---> MET
    met = Variable("MET", is_independent=True, is_binned=True, units="GeV")
    met.values = [item[0] for item in data]

    # Second variable/column ---> Number of observed events
    obs = Variable("Data", is_independent=False,
                   is_binned=False, units="Events")
    obs.values = [item[1] for item in data]

    # Third variable/column ---> Number of predicted events from full fit
    exp_full = Variable("Prediction (SR+CR fit)",
                        is_independent=False, is_binned=False, units="Events")
    exp_full.values = [item[2][0] for item in data]

    unc_full = Uncertainty("total")
    unc_full.values = [item[2][1] for item in data]
    exp_full.uncertainties.append(unc_full)

    # Third variable/column ---> Number of predicted events from CR-only fit
    exp_cr = Variable("Prediction (CR-only fit)",
                      is_independent=False, is_binned=False, units="Events")
    exp_cr.values = [item[3][0] for item in data]

    unc_cr = Uncertainty("total")
    unc_cr.values = [item[3][1] for item in data]
    exp_cr.uncertainties.append(unc_cr)

    table.add_variable(met)
    table.add_variable(obs)
    table.add_variable(exp_full)
    table.add_variable(exp_cr)

    return table

def make_figure_10(outdir):
    table = Table("Unparticle Limits")
    table.location = "Data from figure 10, located on page 22."
    table.description = """The 95% CL upper limits on the Wilson coefficient $\lambda \times (1\mathrm{TeV} / \Lambda_{U})^{d_{U}-1}$ of the unparticle-quark coupling operator."""

    data = np.loadtxt("./input/unpart.txt",skiprows=2)

    d = Variable("Scaling dimension $d_{U}$", is_independent=True, is_binned=False, units="1")
    d.values = data[:,0]

    obs = Variable("Observed Limit", is_independent=False, is_binned=False, units="1")
    obs.values = data[:,2]

    # Expected +- 1 sigma
    exp_1s = Variable("Expected Limit $\pm$ 1 s.d.", is_independent=False, is_binned=False, units="1")
    exp_1s.values = data[:,1]

    unc_1s = Uncertainty("1 s.d.",is_symmetric=False)
    unc_1s.set_values(zip(data[:,3],data[:,4]),nominal=exp_1s.values)
    exp_1s.uncertainties.append(unc_1s)

    # Expected +- 1 sigma
    exp_2s = Variable("Expected Limit $\pm$ 2 s.d.", is_independent=False, is_binned=False, units="1")
    exp_2s.values = data[:,1]
    unc_2s = Uncertainty("2 s.d.",is_symmetric=False)
    unc_2s.set_values(zip(data[:,5],data[:,6]),nominal=exp_2s.values)
    exp_2s.uncertainties.append(unc_2s)

    table.add_variable(d)
    table.add_variable(obs)
    table.add_variable(exp_1s)
    table.add_variable(exp_2s)

    return table

def make_figure_11_right(outdir):
    table = Table("ADD Limits")
    table.location = "Data from figure 11 (right), located on page 22."
    table.description = """The 95% CL lower limits on the reduced Planck mass $M_{D}$ as a function of the number of extra dimensions $d$."""

    data = np.loadtxt("./input/add_md.txt",skiprows=2)

    d = Variable("Number of extra dimension $d$", is_independent=True, is_binned=False, units="1")
    d.values = data[:,0]

    obs = Variable("Observed Limit", is_independent=False, is_binned=False, units="TeV")
    obs.values = data[:,2]

    # Expected +- 1 sigma
    exp_1s = Variable("Expected Limit $\pm$ 1 s.d.", is_independent=False, is_binned=False, units="TeV")
    exp_1s.values = data[:,1]

    unc_1s = Uncertainty("1 s.d.",is_symmetric=False)
    unc_1s.set_values(zip(data[:,3],data[:,4]),nominal=exp_1s.values)
    exp_1s.uncertainties.append(unc_1s)

    # Expected +- 1 sigma
    exp_2s = Variable("Expected Limit $\pm$ 2 s.d.", is_independent=False, is_binned=False, units="TeV")
    exp_2s.values = data[:,1]
    unc_2s = Uncertainty("2 s.d.",is_symmetric=False)
    unc_2s.set_values(zip(data[:,5],data[:,6]),nominal=exp_2s.values)
    exp_2s.uncertainties.append(unc_2s)

    table.add_variable(d)
    table.add_variable(obs)
    table.add_variable(exp_1s)
    table.add_variable(exp_2s)

    return table
def main():
    # Write to this directory
    outdir = "./submission/"

    # Write some files
    submission = Submission()
    submission.tables.append(make_table_4(outdir))
    submission.tables.append(make_figure_10(outdir))
    submission.tables.append(make_figure_11_right(outdir))
    submission.read_abstract("./input/abstract.txt")
    submission.create_files(outdir)


if __name__ == '__main__':
    main()
