#!/bin/bash

echo 'Run displayHistos.sh'
echo $#
echo $1
echo $2
echo $3

source /opt/rh/python27/enable
source /cvmfs/sft.cern.ch/lcg/releases/gcc/4.9.3/x86_64-slc6-gcc49-opt/setup.sh
source /cvmfs/sft.cern.ch/lcg/releases/ROOT/6.06.06-a2c9d/x86_64-slc6-gcc49-opt/bin/thisroot.sh
python -V
root-config --version

python ../HGCTPGValidation/hgctpgvalidation/display/standAloneHGCALTPGhistosCompare.py --refdir $1 --testdir $2 --webdir $3
