#!/bin/bash

echo 'Run displayHistos.sh'
echo $#
echo $1
echo $2
echo $3

source /opt/rh/python27/enable
source /afs/cern.ch/sw/lcg/external/gcc/4.9/x86_64-slc6-gcc49-opt/setup.sh
source /afs/cern.ch/sw/lcg/app/releases/ROOT/6.06.08/x86_64-slc6-gcc49-opt/root/bin/thisroot.sh
python -V
root-config --version

python ../HGCTPGValidation/hgctpgvalidation/display/standAloneHGCALTPGhistosCompare.py --refdir $1 --testdir $2 --webdir $3
