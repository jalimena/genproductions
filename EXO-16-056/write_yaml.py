#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os

from hepdata_lib import *
import numpy as np

def write_figure19(outdir):


    table = Table("figure19")

    reader = RootFileReader("input/fig19_gq/grFinal_DMV-q_qPrime-widewithNarrow-limit.root")

    # X axis: Mediator mass
    mmed = Variable("$m_{med}$")
    mmed.is_independent = True
    mmed.is_binned = False
    mmed.units = "GeV"
    mmed.values = reader.read_graph("graph_expected")["x"]
    table.add_variable(mmed)

    # Y axis: GQ exclusion
    obs = Variable("Observed $g_{q}$ exclusion")
    obs.is_independent = False
    obs.is_binned = False
    obs.units = ""
    obs.values = reader.read_graph("graph_observed")["y"]
    table.add_variable(obs)

  #~ KEY: TGraph	graph_expected;1	
  #~ KEY: TGraph	graph_observed;1	
  #~ KEY: TGraphErrors	graph_expected_p1s;1	
  #~ KEY: TGraphErrors	graph_expected_p2s;1	
  #~ KEY: TGraphErrors	graph_expected_m1s;1	
  #~ KEY: TGraphErrors	graph_expected_m2s;1	
  #~ KEY: TGraph	graph_observedNarrowg_qPrime

    #~ unc1 = Uncertainty("total")
    #~ unc1.values = [item[3][1] for item in data]
    #~ exp_full.uncertainties.append(unc1)

    #~ table.add_variable(exp_full)

    table.write_yaml(outdir)

def make_table_figure7(outdir):
    table = Table("Differential dijet cross-section")
    table.description = "Observed differential dijet cross-section."
    table.location = "Figure 7, located on page 8."
    data = np.loadtxt("./input/fig7/DijetSpectrum_2016full_36-27invfb.txt")
    
    # X axis: Mediator mass
    mmed = Variable("Resonance mass",is_independent = True,is_binned = True,units = "GeV")
    mmed.values_low = [float(x) for x in data[:,0] - data[:,2]]
    mmed.values_high = [float(x) for x in data[:,0] + data[:,3]]

    # Y axis: Differential cross-section
    xs = Variable("Observed")
    xs.is_independent = False
    xs.is_binned = False
    xs.units = "pb/GeV"
    xs.values = [float(x) for x in data[:,1]]

    xs_unc = Uncertainty("Total")
    xs_unc.values = [float(x) for x in data[:,4]]
    xs.uncertainties.append(xs_unc)
    
    table.add_variable(mmed)
    table.add_variable(xs)

    return table

def make_table_figure12(outdir):
    data = np.loadtxt("./input/fig12/LimitsTableObs_2016full_36-27invfb.txt")

    table = Table("Cross-section limits")
    table.location = "Figure 12, located on page 15."
    table.description = "The observed 95% CL upper limits on the product of the cross section, branching fraction, and acceptance for quark-quark, quark-gluon, and gluon-gluon type dijet resonances."

    # X axis: Mediator mass
    mmed = Variable("Resonance mass",is_independent=True,is_binned=False,units="GeV")
    mmed.values = [float(x) for x in data[:,0]]

    # Y axis: Observed limit
    obs_gg = Variable("95% CL upper limits, gg final state", is_independent=False, is_binned=False, units="pb")
    obs_gg.values = [float(x) for x in data[:,1]]

    obs_gq = Variable("95% CL upper limits, gq final state", is_independent=False, is_binned=False, units="pb")
    obs_gq.values = [float(x) for x in data[:,2]]

    obs_qq = Variable("95% CL upper limits, qq final state", is_independent=False, is_binned=False, units="pb")
    obs_qq.values = [float(x) for x in data[:,3]]
    
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

    submission.read_abstract("./input/abstract.txt")

    submission.create_files()



if __name__ == '__main__':
    main()

