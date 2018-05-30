**Repository to store everything HEPData submission files in EXO.**

The scripts rely heavily on the [hepdata_lib](https://github.com/clelange/hepdata_lib) python library.
Please make sure to set it up before trying to use the files in this repository (see the [documentation](https://hepdata-lib.readthedocs.io/en/latest/]))

**Usage**
```
# Set up the repository

# Either via ssh
git clone ssh://git@gitlab.cern.ch:7999/cms-exo-mci/exo-hepdata.git

# Or via https
git clone https://gitlab.cern.ch/cms-exo-mci/exo-hepdata.git

cd exo-hepdata

```

**Example**
```
# Run an example
cd EXO-16-052
./write_yaml.py

ls
>>> submission  submission.tar.gz  write_yaml.py
```

```submission``` is a folder containing individual yaml files.  You can open them in a text editor.
```submission.tar.gz``` is an archive ready for uploading to HEPData.

You can test this by going to

https://www.hepdata.net/record/sandbox

and uploading the tar file to your private sandbox (no worries, this is not published)
HEPData will then show you what your entry would look like.
