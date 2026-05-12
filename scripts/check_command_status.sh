#!/usr/bin/env bash

# $1 status variable
# $2 stage name

# If the script displayHistos.py failed, the pipeline stops
if [ $1 -gt 0 ];
then
    echo ' Error in stage ' $2 ', with status=' $1
    cat ./out_err >&2
    exit $1
else
    echo ' The stage ' $2 ' completed successufully!'
fi
