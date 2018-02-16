#!/bin/csh
set TOPPATH=`pwd`
if ( $?PYTHONPATH ) then
    setenv PYTHONPATH "${PYTHONPATH}:${TOPPATH}/lib"
else
    setenv PYTHONPATH "${TOPPATH}/lib"
endif
