**Repository to store everything around HEPData use in EXO.**

The goal is to

a) provide libraries, scripts, etc. to assisst analyzers in creating HEPData submissions.

b) to store the submission files.



**Usage**
```
# Set up the repository
git clone ssh://git@gitlab.cern.ch:7999/cms-exo-mci/exo-hepdata.git
cd exo-hepdata

# Make sure the libraries are part of the python PATH.
source setenv.sh
```

**Example**
```
# Run an example
cd EXO-16-052
./write_yaml.py

ls
>>> submission  submission.tar.gz  write_yaml.py
```

"submission" is a folder containing individual yaml files. 
submission.tar.gz is an archive ready for uploading to HEPData.

You can test this by going to

https://www.hepdata.net/record/sandbox

and uploading the tar file to your private sandbox (no worries, this is not published)
HEPData will then show you what your entry would look like.

