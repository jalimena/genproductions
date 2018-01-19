#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os

from hepdata_lib import *
import numpy as np


def make_table_figure19(outdir):
    # Input provided as tree (Yalcin Guler)
    # Each branch holds one variable/variation
    reader = RootFileReader("input/fig19/gq_WideLimitTree.root")

    table = Table("Coupling limits (DM mediator)")
    table.description = "The observed and expected 95% CL upper limits on the universal quark coupling $g_{q}$ as a function of resonance mass for a vector mediator of interactions between quarks and dark matter."

    table.location = "Data from Figure 19, located on page 24."
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

    # For 4.1 TeV, there is no observed limit
    # The input file incorrectly says "1" here
    # So we just replace that entry by "-"
    assert(obs.values[-1] == 1)
    obs.values[-1] = "-"

    exp_1sd = Variable("Expected $g_{q}$ exclusion $\pm$ 1 s.d.",
                       is_independent=False, is_binned=False, units="")
    exp_1sd.values = reader.read_tree("xsecTree", "xsecULExp_PFDijet2016")

    exp_2sd = Variable("Expected $g_{q}$ exclusion $\pm$ 2 s.d.",
                       is_independent=False, is_binned=False, units="")
    exp_2sd.values = reader.read_tree("xsecTree", "xsecULExp_PFDijet2016")

    unc1 = Uncertainty("1 s.d.")
    unc1.is_symmetric = False
    unc1.set_values(
        zip(
            reader.read_tree(
                "xsecTree", "xsecULExpMinus_PFDijet2016"
            ),
            reader.read_tree(
                "xsecTree", "xsecULExpPlus_PFDijet2016"
            )
        ), nominal=exp_1sd.values)

    unc2 = Uncertainty("2 s.d.")
    unc2.is_symmetric = False
    unc2.set_values(
        zip(
            reader.read_tree(
                "xsecTree", "xsecULExpMinus2_PFDijet2016"
            ), reader.read_tree(
                "xsecTree", "xsecULExpPlus2_PFDijet2016"
            )), nominal=exp_2sd.values)

    exp_1sd.uncertainties.append(unc1)
    exp_2sd.uncertainties.append(unc2)

    table.add_variable(exp_1sd)
    table.add_variable(exp_2sd)
    table.add_variable(obs)

    return table


def make_table_figure7_left(outdir):
    # Input provided as text file (Frederico Preiato, Giulia D'Imperio)
    # Each columns holds one variable or uncertainty
    data = np.loadtxt("./input/fig7/DijetSpectrum_2016full_36-27invfb.txt")

    table = Table("Differential dijet cross-section (Low mass analysis)")
    table.description = "Observed differential dijet cross-section."
    table.location = "Data from Figure 7 (left), located on page 8."
    table.keywords["observables"] = ["DSIG/DM"]

    # Border between low and high mass entries
    border = 25


    # X axis: Mediator mass
    mmed = Variable("Dijet mass", is_independent=True,
                    is_binned=True, units="GeV")
    mmed.values = zip(data[:, 0] - data[:, 2], data[:, 0] + data[:, 3])
    mmed.values = mmed.values[:border]

    # Low mass analysis
    xs_low = Variable("Observed")
    xs_low.is_independent = False
    xs_low.is_binned = False
    xs_low.units = "pb/TeV"

    # Multiply by a thousand to go from pb / GeV -> pb / TeV
    xs_low.values = list(1e3 * data[:border, 1])

    xs_low_unc = Uncertainty("Total",is_symmetric=False)
    xs_low_unc.values = list(zip(-1e3 * data[:border, 4],1e3 * data[:border, 5]))

    xs_low.uncertainties.append(xs_low_unc)

    table.add_variable(mmed)
    table.add_variable(xs_low)
    return table

def make_table_figure7_right(outdir):
    # Input provided as text file (Frederico Preiato, Giulia D'Imperio)
    # Each columns holds one variable or uncertainty
    data = np.loadtxt("./input/fig7/DijetSpectrum_2016full_36-27invfb.txt")

    table = Table("Differential dijet cross-section (High mass analysis)")
    table.description = "Observed differential dijet cross-section."
    table.location = "Data from Figure 7 (right), located on page 8."
    table.keywords["observables"] = ["DSIG/DM"]

    # Border between low and high mass entries
    border = 25

    # X axis: Mediator mass
    mmed = Variable("Dijet mass", is_independent=True,
                    is_binned=True, units="GeV")
    mmed.values = zip(data[:, 0] - data[:, 2], data[:, 0] + data[:, 3])
    mmed.values = mmed.values[border:]

    # Low mass analysis
    xs_high = Variable("Observed")
    xs_high.is_independent = False
    xs_high.is_binned = False
    xs_high.units = "pb/TeV"

    # Multiply by a thousand to go from pb / GeV -> pb / TeV
    xs_high.values = list(1e3 * data[border:, 1])

    xs_high_unc = Uncertainty("Total",is_symmetric=False)
    xs_high_unc.values = list(zip(-1e3 * data[border:, 4], 1e3 * data[border:, 5]))

    xs_high.uncertainties.append(xs_high_unc)

    table.add_variable(mmed)
    table.add_variable(xs_high)

    return table


def make_table_figure12(outdir):
    # Input provided as text file (Frederico Preiato, Giulia D'Imperio)
    # Each columns holds one variable
    data = np.loadtxt("./input/fig12/LimitsTableObs_2016full_36-27invfb.txt")

    # X axis: Mediator mass
    mmed = Variable("Resonance mass", is_independent=True,
                    is_binned=False, units="GeV")
    mmed.values = data[:, 0]

    # Y axis: Observed limit
    obs_gg = Variable("95% CL upper limits, gg final state",
                      is_independent=False, is_binned=False, units="pb")
    obs_gg.values = data[:, 1]

    obs_gq = Variable("95% CL upper limits, gq final state",
                      is_independent=False, is_binned=False, units="pb")
    obs_gq.values = data[:, 2]

    obs_qq = Variable("95% CL upper limits, qq final state",
                      is_independent=False, is_binned=False, units="pb")
    obs_qq.values = data[:, 3]

    table = Table("Cross-section limits")
    table.location = "Data from Figure 12, located on page 15."
    table.keywords["observables"] = ["DSIG/DM"]
    table.description = "The observed 95% CL upper limits on the product of the cross section, branching fraction, and acceptance for quark-quark, quark-gluon, and gluon-gluon type dijet resonances."

    table.add_variable(mmed)
    table.add_variable(obs_gg)
    table.add_variable(obs_gq)
    table.add_variable(obs_qq)

    return table


def make_table_figure13(outdir):

    reader = RootFileReader("input/fig13/save.root")
    data_obs_low = reader.read_graph("observed_low")
    data_obs_high = reader.read_graph("observed_high")

    data_exp_low = reader.read_graph("expected_low")
    data_exp_1s_low_up = reader.read_graph("expected_1s_low_up")
    data_exp_1s_low_down = reader.read_graph("expected_1s_low_down")
    data_exp_2s_low_up = reader.read_graph("expected_2s_low_up")
    data_exp_2s_low_down = reader.read_graph("expected_2s_low_down")

    data_exp_high = reader.read_graph("expected_high")
    data_exp_1s_high_up = reader.read_graph("expected_1s_high_up")
    data_exp_1s_high_down = reader.read_graph("expected_1s_high_down")
    data_exp_2s_high_up = reader.read_graph("expected_2s_high_up")
    data_exp_2s_high_down = reader.read_graph("expected_2s_high_down")

    assert(data_obs_low["x"] == data_exp_low["x"])
    assert(data_obs_high["x"] == data_exp_high["x"])

    # X axis: Mediator mass
    mmed = Variable("Resonance mass", is_independent=True,
                    is_binned=False, units="GeV")
    mmed.values = data_obs_low["x"] + data_obs_high["x"]

    obs = Variable("Observed $g_{q}'$ exclusion",
                   is_independent=False, is_binned=False, units="1")
    obs.values = data_obs_low["y"] + data_obs_high["y"]

    exp_1sd = Variable("Expected $g_{q}'$ exclusion $\pm$ 1 s.d.",
                       is_independent=False, is_binned=False, units="1")
    exp_1sd.values = data_exp_low["y"] + data_exp_high["y"]

    exp_2sd = Variable("Expected $g_{q}'$ exclusion $\pm$ 2 s.d.",
                       is_independent=False, is_binned=False, units="1")
    exp_2sd.values = data_exp_low["y"] + data_exp_high["y"]

    unc1 = Uncertainty("1 s.d.")
    unc1.is_symmetric = False
    unc1.set_values(zip(data_exp_1s_low_down["y"] + data_exp_1s_high_down["y"],
                        data_exp_1s_low_up["y"] + data_exp_1s_high_up["y"]), nominal=exp_1sd.values)

    unc2 = Uncertainty("2 s.d.")
    unc2.is_symmetric = False
    unc2.set_values(zip(data_exp_2s_low_down["y"] + data_exp_2s_high_down["y"],
                        data_exp_2s_low_up["y"] + data_exp_2s_high_up["y"]), nominal=exp_2sd.values)

    exp_1sd.uncertainties.append(unc1)
    exp_2sd.uncertainties.append(unc2)

    table = Table("Coupling limits (Quark only)")
    table.location = "Data from Figure 13, located on page 17."
    table.keywords["observables"] = ["GQ"]
    table.description = "The observed and expected 95% CL upper limits on the universal quark coupling $g_{q}'$ as a function of resonance mass for a leptophobic Z' resonance that only couples to quarks."

    table.add_variable(mmed)
    table.add_variable(obs)
    table.add_variable(exp_1sd)
    table.add_variable(exp_2sd)

    return table

    #~ def parse_tylers_graph(data):
    #~ '''Get upper and lower quantiles from an unordered set of data.
    #~ It is assumed that there are two y valeus for each x value.
    #~ Y values are sorted by x value and the bigger/smaller one of the two y values is used for up/down quantiles.'''
    #~ split = defaultdict(list)
    #~ for x,y in zip(data["x"],data["y"]):
    #~ split[x].append(y)

    #~ for key in sorted(split.keys()):
    #~ print key, split[key]
    #~ list_unc = []
    #~ for entry in split.values():
    #~ print entry
    #~ assert(len(entry)==2)
    #~ list_unc.append(tuple(sorted(entry)))

    #~ return list_unc


def main():
    # Write to this directory
    outdir = "./submission/"

    submission = Submission()
    submission.add_table(make_table_figure7_left(outdir))
    submission.add_table(make_table_figure7_right(outdir))
    submission.add_table(make_table_figure12(outdir))
    submission.add_table(make_table_figure19(outdir))
    submission.add_table(make_table_figure13(outdir))
    submission.read_abstract("./input/abstract.txt")

    for table in submission.tables:
        table.keywords["reactions"] = ["P P --> JET JET X"]
        table.keywords["cmenergies"] = [13000]
    submission.create_files(outdir)


if __name__ == '__main__':
    main()
