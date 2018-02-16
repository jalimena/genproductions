#!/usr/bin/env python
#-*- coding:utf-8 -*-
from hepdata_lib import *

'''This is a simple example script to demonstrate how to make a submission.'''

# Let's pretend we want to publish a table of mass limits
# We calculated the limit for different values of a parameter x
data_x = [ 1.0, 3.5, 9.3, 15.6 ]
data_m = [ 1234.7, 1001.4, 734.3, 599.8 ]

### Step 1: Make a table
table = Table("Mass exclusion limits as a function of x")
table.location = "The data in this table is located on page 4 of the paper."
table.description = "These limits assume a branching fraction of..."

### Step 2: Make the variables and add them to the table
x = Variable(
            "Parameter x",         # Name of the variable
            is_independent=True,   # "Independent" is typically what we put on the x axis
            is_binned=False,       # We just have discrete values for x, no binning involved
            units="GeV"            # x is a kind of energy, so we give it in GeV
            )

x.values = data_x
table.add_variable(x)

m = Variable(
            "Mass limit",
            is_independent=False, # The value of m depends on the value of x
            is_binned=False,
            units="GeV"
            )
m.values = data_m
table.add_variable(m)



### Step 3: Create a Submission object and add the table to it
submission = Submission()
submission.tables.append(table)

# Write output
submission.create_files("./submission/")


# That's it!
# You should now find a "submission.tar.gz" file in the folder where you executed this script.
# This file is ready to be uploaded to hepdata.
