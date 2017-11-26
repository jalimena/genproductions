#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os

from hepdata_lib import *
import numpy as np


def make_table_figure19(outdir):
    # Input provided as tree (Yalcin Guler)
    # Each branch holds one variable/variation
    reader = RootFileReader("input/fig19/gq_WideLimitTree.root")

    table = Table("Limits on universal quark coupling")
    table.description = "."

    table.location = "Figure 19, located on page 24."
    table.keywords["observables"] = ["GV"]

    # X axis: Mediator mass
    mmed = Variable("$M_{Med}$")
    mmed.is_independent = True
    mmed.is_binned = False
    mmed.units = "GeV"
    mmed.values = reader.read_tree("xsecTree", "mass")
    table.add_variable(mmed)

    # Y axis: GQ exclusion
    obs = Variable("Observed $g_{q}$ exclusion",
                   is_independent=False, is_binned=False, units="")
    obs.values = reader.read_tree("xsecTree", "xsecULObs_PFDijet2016")

    exp = Variable("Expected $g_{q}$ exclusion",
                   is_independent=False, is_binned=False, units="")
    exp.values = reader.read_tree("xsecTree", "xsecULExp_PFDijet2016")

    unc1 = Uncertainty("1 s.d.")
    unc1.is_symmetric = False
    unc1.set_values_up(reader.read_tree(
        "xsecTree", "xsecULExpPlus_PFDijet2016"), nominal=exp.values)
    unc1.set_values_down(reader.read_tree(
        "xsecTree", "xsecULExpMinus_PFDijet2016"), nominal=exp.values)

    unc2 = Uncertainty("2 s.d.")
    unc2.is_symmetric = False
    unc2.set_values_up(reader.read_tree(
        "xsecTree", "xsecULExpPlus2_PFDijet2016"), nominal=exp.values)
    unc2.set_values_down(reader.read_tree(
        "xsecTree", "xsecULExpMinus2_PFDijet2016"), nominal=exp.values)

    exp.uncertainties.append(unc1)
    exp.uncertainties.append(unc2)

    table.add_variable(exp)
    table.add_variable(obs)

    return table


def make_table_figure7(outdir):
    # Input provided as text file (Frederico Preiato, Giulia D'Imperio)
    # Each columns holds one variable or uncertainty
    data = np.loadtxt("./input/fig7/DijetSpectrum_2016full_36-27invfb.txt")

    table = Table("Differential dijet cross-section")
    table.description = "Observed differential dijet cross-section."
    table.location = "Figure 7, located on page 8."
    table.keywords["observables"] = ["DSIG/DM"]

    # X axis: Mediator mass
    mmed = Variable("Resonance mass", is_independent=True,
                    is_binned=True, units="GeV")
    mmed.values_low = [float(x) for x in data[:, 0] - data[:, 2]]
    mmed.values_high = [float(x) for x in data[:, 0] + data[:, 3]]

    # Y axis: Differential cross-section
    xs = Variable("Observed")
    xs.is_independent = False
    xs.is_binned = False
    xs.units = "pb/GeV"
    xs.values = [float(x) for x in data[:, 1]]

    xs_unc = Uncertainty("Total")
    xs_unc.values = [float(x) for x in data[:, 4]]
    xs.uncertainties.append(xs_unc)

    table.add_variable(mmed)
    table.add_variable(xs)

    return table


def make_table_figure12(outdir):
    # Input provided as text file (Frederico Preiato, Giulia D'Imperio)
    # Each columns holds one variable
    data = np.loadtxt("./input/fig12/LimitsTableObs_2016full_36-27invfb.txt")

    table = Table("Cross-section limits")
    table.location = "Figure 12, located on page 15."
    table.keywords["observables"] = ["DSIG/DM"]
    table.description = "The observed 95% CL upper limits on the product of the cross section, branching fraction, and acceptance for quark-quark, quark-gluon, and gluon-gluon type dijet resonances."

    # X axis: Mediator mass
    mmed = Variable("Resonance mass", is_independent=True,
                    is_binned=False, units="GeV")
    mmed.values = [float(x) for x in data[:, 0]]

    # Y axis: Observed limit
    obs_gg = Variable("95% CL upper limits, gg final state",
                      is_independent=False, is_binned=False, units="pb")
    obs_gg.values = [float(x) for x in data[:, 1]]

    obs_gq = Variable("95% CL upper limits, gq final state",
                      is_independent=False, is_binned=False, units="pb")
    obs_gq.values = [float(x) for x in data[:, 2]]

    obs_qq = Variable("95% CL upper limits, qq final state",
                      is_independent=False, is_binned=False, units="pb")
    obs_qq.values = [float(x) for x in data[:, 3]]

    table.add_variable(mmed)
    table.add_variable(obs_gg)
    table.add_variable(obs_gq)
    table.add_variable(obs_qq)

    return table


def main():
    # Write to this directory
    outdir = "./submission/"

    submission = Submission()
    submission.add_table(make_table_figure7(outdir))
    submission.add_table(make_table_figure12(outdir))
    submission.add_table(make_table_figure19(outdir))
    submission.read_abstract("./input/abstract.txt")

    for table in submission.tables:
        table.keywords["reactions"] = ["P P --> JET JET X"]
        table.keywords["cmenergies"] = [13000]
    submission.create_files(outdir)


if __name__ == '__main__':
    main()
