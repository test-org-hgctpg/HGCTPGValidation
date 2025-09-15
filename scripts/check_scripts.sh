#!/bin/bash
# $1 the status of previous command
# $2 script file name
# Usage check_scripts.sh $? {script_file}_USER.py

# If the script file exists and is not empty => OK
# If this not the case the scrip returns status 1
if [ -s $2 ] ; then
    echo "The script " $2 "was created.";
else
    echo "     "
    echo "!!!! cmsDriver failed to execute! The script " $2 "has not been created!"; exit 1;
fi
