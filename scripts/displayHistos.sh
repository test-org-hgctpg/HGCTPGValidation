#!/bin/bash

echo 'Run displayHistos.sh'
echo $#
echo $1
echo $2
echo $3

# Config at Cern
#source /opt/rh/python27/enable
#source /cvmfs/sft.cern.ch/lcg/releases/gcc/4.9.3/x86_64-slc6-gcc49-opt/setup.sh
#source /cvmfs/sft.cern.ch/lcg/releases/ROOT/6.06.06-a2c9d/x86_64-slc6-gcc49-opt/bin/thisroot.sh

# Config at LLR, working with sl6 releases
source /usr/share/Modules/init/bash
module use /opt/exp_soft/vo.llr.in2p3.fr/modulefiles
module swap python/3.6.3 python/2.7.10
source /opt/exp_soft/llr/root/v6.06.00-el6-gcc48/etc/init.sh

# at LLR, working with sl7 releases
#module use /opt/exp_soft/vo.llr.in2p3.fr/modulefiles_el7/
#module load python/3.6.6

python -V
root-config --version

python ../HGCTPGValidation/hgctpgvalidation/display/standAloneHGCALTPGhistosCompare.py --refdir $1 --testdir $2 --webdir $3
