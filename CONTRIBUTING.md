**Code style**

Please make sure to check your code style before making a pull request.

A first stop is to apply the ```autopep8``` code checker. 
This will take care of white space, line breaks, etc.

```
# WARNING: This will change your files
# WARNING: Make sure to have a backup if needed

pip install autopep8 --user
python -m autopep8 --in-place ${FILE}
```


It is also recommended to run ```pylint```. 
This will also tell you about more high-level code
structure aspects:

```
# This does not change any files

pip install pylint --user
pylint ${FILE}
```

