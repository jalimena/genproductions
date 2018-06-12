#!/usr/bin/env python
import os, sys
import numpy as np
from hepdata_lib import *

#\\sigma(pp \\rightarrow \\tilde{g}\\tilde{g}) ~\\mathcal{B}(\\tilde{g} \\rightarrow q\\bar{q}\\tilde{\\chi}^{0})

def make_figure_6_graph_obs(outdir):
    reader = RootFileReader("data/excludedRegionStop_CWR_new.root")
    points_obs = reader.read_graph("70y")

    stopMass = Variable("Top squark mass", is_independent=True, is_binned=False, units="GeV")
    stopMass.values = points_obs["x"]

    neutralinoMassObs = Variable("Neutralino mass, observed", is_independent=False, is_binned=False, units="GeV")
    neutralinoMassObs.values = points_obs["y"]

    table = Table("Figure 6 upper right observed")
    table.location = "Data from Figure 6 (upper right), located on page 18."
    table.description = """The 95% CL upper limits in the neutralino mass vs.~top squark mass plane, for lifetimes between 10 $\mu$s and 1000 s, for combined 2015 and 2016 data for the calorimeter search. The mostly triangular region shows the excluded observed region. We show top squarks that undergo a two-body decay."""
    table.add_variable(stopMass)
    table.add_variable(neutralinoMassObs)

    return table

def make_figure_6_graph_exp(outdir):
    reader = RootFileReader("data/excludedRegionStop_CWR_new.root")
    points_exp = reader.read_graph("expExcl70")

    stopMass = Variable("Top squark mass", is_independent=True, is_binned=False, units="GeV")
    stopMass.values = points_exp["x"]

    neutralinoMassExp = Variable("Neutralino mass, expected", is_independent=False, is_binned=False, units="GeV")
    neutralinoMassExp.values = points_exp["y"]

    table = Table("Figure 6 upper right expected")
    table.location = "Data from Figure 6 (upper right), located on page 18."
    table.description = """The 95% CL upper limits in the neutralino mass vs.~top squark mass plane, for lifetimes between 10 $\mu$s and 1000 s, for combined 2015 and 2016 data for the calorimeter search. The mostly triangular region shows the excluded expected region. We show top squarks that undergo a two-body decay."""
    table.add_variable(stopMass)
    table.add_variable(neutralinoMassExp)

    return table

def make_figure_6_graph_expP1(outdir):
    reader = RootFileReader("data/excludedRegionStop_CWR_new.root")
    points_exp_p1 = reader.read_graph("expExcl70p1")

    stopMass = Variable("Top squark mass", is_independent=True, is_binned=False, units="GeV")
    stopMass.values = points_exp_p1["x"]

    neutralinoMassExpP1 = Variable("Neutralino mass, expected + 1 s.d.", is_independent=False, is_binned=False, units="GeV")
    neutralinoMassExpP1.values = points_exp_p1["y"]

    table = Table("Figure 6 upper right expected plus 1 sd")
    table.location = "Data from Figure 6 (upper right), located on page 18."
    table.description = """The 95% CL upper limits in the neutralino mass vs.~top squark mass plane, for lifetimes between 10 $\mu$s and 1000 s, for combined 2015 and 2016 data for the calorimeter search. The mostly triangular region shows the excluded expected +1 s.d. region. We show top squarks that undergo a two-body decay."""
    table.add_variable(stopMass)
    table.add_variable(neutralinoMassExpP1)

    return table

def make_figure_6_graph_expM1(outdir):
    reader = RootFileReader("data/excludedRegionStop_CWR_new.root")
    points_exp_m1 = reader.read_graph("expExcl70m1")

    stopMass = Variable("Top squark mass", is_independent=True, is_binned=False, units="GeV")
    stopMass.values = points_exp_m1["x"]

    neutralinoMassExpM1 = Variable("Neutralino mass, expected - 1 s.d.", is_independent=False, is_binned=False, units="GeV")
    neutralinoMassExpM1.values = points_exp_m1["y"]    

    table = Table("Figure 6 upper right expected minus 1 sd")
    table.location = "Data from Figure 6 (upper right), located on page 18."
    table.description = """The 95% CL upper limits in the neutralino mass vs.~top squark mass plane, for lifetimes between 10 $\mu$s and 1000 s, for combined 2015 and 2016 data for the calorimeter search. The mostly triangular region shows the excluded expected -1 s.d. region. We show top squarks that undergo a two-body decay."""
    table.add_variable(stopMass)
    table.add_variable(neutralinoMassExpM1)

    return table

def make_figure_6_upper_right(outdir):
    reader = RootFileReader("data/excludedRegionStop_CWR_new.root")
    points = reader.read_hist_2d("stopxsec")

    stopMass = Variable("Top squark mass", is_independent=True, is_binned=True, units="GeV")
    stopMass.values = [(x-1,x+1) for x in points["x"]]

    neutralinoMass = Variable("Neutralino mass", is_independent=True, is_binned=True, units="GeV")
    neutralinoMass.values = [(y-0.8125,y+0.8125) for y in points["y"]]

    limit = Variable("95% CL upper limit on $\\sigma(pp \\rightarrow \\tilde{t}\\tilde{t}) ~\\mathcal{B}(\\tilde{t} \\rightarrow t\\tilde{\\chi}^{0})$",is_independent=False, is_binned=False,units="fb")
    limit.values = points["z"]

    table = Table("Figure 6 upper right 2D limits")
    table.location = "Data from Figure 6 (upper right), located on page 18."
    table.description = """The 95% CL upper limits in the neutralino mass vs.~top squark mass plane, for lifetimes between 10 $\mu$s and 1000 s, for combined 2015 and 2016 data for the calorimeter search. The color map indicates the 95% CL upper limits on $\mathcal{B}\sigma$. We show top squarks that undergo a two-body decay."""
    table.add_variable(stopMass)
    table.add_variable(neutralinoMass)
    table.add_variable(limit)

    return table

def main():
    # Write to this directory
    outdir = "./submission_limits_calo_stop_2d_graphs/"

    # Write some files 
    submission = Submission()
    submission.tables.append(make_figure_6_graph_obs(outdir))
    submission.tables.append(make_figure_6_graph_exp(outdir))
    submission.tables.append(make_figure_6_graph_expP1(outdir))
    submission.tables.append(make_figure_6_graph_expM1(outdir))
    submission.tables.append(make_figure_6_upper_right(outdir))
    #submission.read_abstract("./input/abstract.txt")
    submission.create_files(outdir)


if __name__ == '__main__':
    main()
