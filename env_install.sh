#!/bin/bash

# For sl9 please check
# module use /opt/exp_soft/vo.llr.in2p3.fr/modulefiles_el9/
# module avail

# These variables are get also in displayHistos.py in order to set the appropriate environment
# CERN         1
# LLR, sl9     2
simu_env=2
export simu_env

if [ $simu_env -eq 1 ]
then
    # at CERN
    source /opt/rh/rh-python36/enable
    #echo 'Working at CERN environment'
elif [ $simu_env -eq 2 ]
then
    # at LLR, working with sl7 releases
    module use /opt/exp_soft/vo.llr.in2p3.fr/modulefiles_el9/
    module purge
    module load python/latest
    #echo 'Working at LLR in sl9 environment'
fi

uname -a
python --version
