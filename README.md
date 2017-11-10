Repository to store everything around HEPData use in EXO.

The goal is to

a) provide libraries, scripts, etc. to assisst analyzers in creating HEPData submissions.

b) to store the submission files.



Usage

To use the repository

```
# Set up the repository
git clone ssh://git@gitlab.cern.ch:7999/cms-exo-mci/exo-hepdata.git
cd exo-hepdata
source setenv.sh

# Run an example
cd EXO-16-052
./write_yaml.py

ls
```

