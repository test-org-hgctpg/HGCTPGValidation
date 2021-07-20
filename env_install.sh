#!/bin/bash

# Before starting please check the python2 and python3 available versions on polui
# For sl6
# module use /opt/exp_soft/vo.llr.in2p3.fr/modulefiles
# module avail
# For sl7 please check
# module use /opt/exp_soft/vo.llr.in2p3.fr/modulefiles_el7/
# module avail

# Thise variables are get also in displayHistos.sh in order to set the appropriate environment
# CERN         1
# LLR, sl6     2
# LLR, sl7     3
simu_env=3
export simu_env

if [ $simu_env -eq 1 ]
then
    # at CERN
    source /opt/rh/rh-python36/enable
    echo 'Working at CERN environment'
elif [ $simu_env -eq 2 ]
then
    # at LLR, working with sl6 releases
    source /usr/share/Modules/init/bash
    module use /opt/exp_soft/vo.llr.in2p3.fr/modulefiles
    # useful in case we rerun only the simulation step
    module purge python
    module load python/3.6.3
    echo 'Working at LLR in sl6 environment'
else [ $simu_env -eq 3 ]
    # at LLR, working with sl7 releases
    module use /opt/exp_soft/vo.llr.in2p3.fr/modulefiles_el7/
    # useful in case we rerun only the simulation step
    module purge
    module load python/3.7.0
    module load compilers/gcc/9.x.x
    source /opt/exp_soft/llr/root/vv6.20.06-el7-gcc9-py37/etc/init.sh
    echo 'Working at LLR in sl7 environment'
fi

uname -a
python --version
