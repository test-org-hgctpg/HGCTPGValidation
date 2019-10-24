#!/bin/bash

# at CERN
#source /opt/rh/rh-python36/enable

# at LLR, working with sl6 releases
#source /usr/share/Modules/init/bash
#module use /opt/exp_soft/vo.llr.in2p3.fr/modulefiles
#module load python/3.6.3

# at LLR, working with sl7 releases
module use /opt/exp_soft/vo.llr.in2p3.fr/modulefiles_el7/
module unload python/3.6.3
module load python/3.6.6
uname -a
python --version
