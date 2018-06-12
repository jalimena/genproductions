python deltaTDT_muon.py
python deltaTRPC_muon.py
python ereco_calo_gluino2b_600GeV.py
python ereco_calo_gluino2b_1200GeV.py
python ereco_calo_gluino2b_1800GeV.py
python ereco_calo_stop2b_400GeV.py
python ereco_calo_stop2b_1000GeV.py
python ereco_calo_stop2b_600GeV.py
python ereco_calo_g3b_800and1000GeV.py
python ereco_calo_g3b_1800GeV.py
python HepData_muon_extrapolating.py
python limitsHepData_muon_glifetime.py
python limitsHepData_muon_gmass.py
python limitsHepData_muon_mchampmass.py
python limitsHepData_muon_mlifetime.py
python limitsHepData_sp_g2bmass.py
python limitsHepData_sp_g2bxsec.py
python limitsHepData_sp_g3bmass.py
python limitsHepData_sp_g3bxsec.py
python limitsHepData_sp_stopmass.py
python limitsHepData_sp_stopxsec.py
mkdir to_submit
mv lim_* to_submit/
mv background_extrapolating.yaml to_submit/
mv ereco_*.yaml to_submit/
mv delta*.yaml to_submit/

#from exo-hepdata, need to be copied to the rest
python limitsHepData_sp_g2b_2d_graphs.py
python limitsHepData_sp_stop_2d_graphs.py
python limitsHepData_sp_g3b_2d_graphs.py
cp submission_limits_calo_g2b_2d_graphs/figure*.yaml to_submit/
cp submission_limits_calo_stop_2d_graphs/figure*.yaml to_submit/
cp submission_limits_calo_g3b_2d_graphs/figure*.yaml to_submit/
cat submission.yaml submission_limits_calo_g2b_2d_graphs/submission.yaml submission_limits_calo_stop_2d_graphs/submission.yaml submission_limits_calo_g3b_2d_graphs/submission.yaml > to_submit/submission.yaml

#need to adjust to_submit/submission.yaml, then do this tar command:
#tar -cvzf submission.tar.gz to_submit/
