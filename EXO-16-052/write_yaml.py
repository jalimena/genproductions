#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os

from hepdata_lib import *


def write_table_4(outdir):
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
        [(500, 13000), 1, (1.63, 0.24), (1.57, 0.33)]
    ]

    table = Table("table4")
    # First variable/column ---> MET
    met = Variable("MET")
    met.is_independent = True
    met.is_binned = True
    met.units = "GeV"
    met.values_low = [item[0][0] for item in data]
    met.values_high = [item[0][1] for item in data]
    table.add_variable(met)

    # Second variable/column ---> Number of observed events
    obs = Variable("Observed")
    obs.is_independent = False
    obs.is_binned = False
    obs.units = "Events"
    obs.values = [item[1] for item in data]
    table.add_variable(obs)

    # Third variable/column ---> Number of predicted events from full fit
    exp_full = Variable("Prediction (SR+CR fit)")
    exp_full.is_independent = False
    exp_full.is_binned = False
    exp_full.units = "Events"
    exp_full.values = [item[2][0] for item in data]

    unc1 = Uncertainty("total")
    unc1.values = [item[2][1] for item in data]
    exp_full.uncertainties.append(unc1)

    table.add_variable(exp_full)

    # Third variable/column ---> Number of predicted events from CR-only fit
    exp_full = Variable("Prediction (CR-only fit)")
    exp_full.is_independent = False
    exp_full.is_binned = False
    exp_full.units = "Events"
    exp_full.values = [item[3][0] for item in data]

    unc1 = Uncertainty("total")
    unc1.values = [item[3][1] for item in data]
    exp_full.uncertainties.append(unc1)

    table.add_variable(exp_full)

    table.write_yaml(outdir)


def write_submission_file(outdir):
    # Write submission file
    submission = {}
    submission["name"] = "Table 4"
    submission["description"] = "A histogram we really care about. It is super important. That's why it has a description."
    submission["keywords"] = [
        {"name": "Analysis groups", "values": ["EXO", "EXO-METX"]}]
    submission["data_file"] = "table4.yaml"

    if(not os.path.exists(outdir)):
        os.makedirs(outdir)
    with open(os.path.join(outdir, 'submission.yaml'), 'w') as outfile:
        yaml.dump(submission, outfile, default_flow_style=False)


def main():
    # Write to this directory
    outdir = "./submission/"

    # Write some files
    write_table_4(outdir)
    write_submission_file(outdir)

    # Put them into a tar file
    import tarfile
    tar = tarfile.open("submission.tar.gz", "w:gz")
    for f in find_all_matching(outdir, "*.yaml"):
        tar.add(f)
    tar.close()


if __name__ == '__main__':
    main()
