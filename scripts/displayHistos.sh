#!/bin/bash

echo 'Run displayHistos.sh'
echo $#
echo $1
echo $2
echo $3
echo $simu_env

if [ $simu_env -eq 1 ]
then
    # Config at Cern
    source /opt/rh/python27/enable
    source /cvmfs/sft.cern.ch/lcg/releases/gcc/4.9.3/x86_64-slc6-gcc49-opt/setup.sh
    source /cvmfs/sft.cern.ch/lcg/releases/ROOT/6.06.06-a2c9d/x86_64-slc6-gcc49-opt/bin/thisroot.sh
elif [ $simu_env -eq 2 ]
then
    # Config at LLR in sl6, switch to python2
    source /usr/share/Modules/init/bash
    module use /opt/exp_soft/vo.llr.in2p3.fr/modulefiles
    module swap python/3.6.3 python/2.7.10
    source /opt/exp_soft/llr/root/v6.06.00-el6-gcc48/etc/init.sh
else [ $simu_env -eq 3 ]
    # Config at LLR in sl7, switch to python2
    #module use /opt/exp_soft/vo.llr.in2p3.fr/modulefiles_el7/
    source /usr/share/Modules/init/bash
    module use /opt/exp_soft/vo.llr.in2p3.fr/modulefiles
    module swap python/3.6.6 python/2.7.10
    source /opt/exp_soft/llr/root/v6.06.00-el6-gcc48/etc/init.sh
fi

echo 'The Python version was changed to '
python -V
echo 'The ROOT version is '
root-config --version

find . -name "out_ref.log" | xargs grep "TimeModule>" > TimingInfo_ref.txt
find . -name "out_test.log" | xargs grep "TimeModule>" > TimingInfo_test.txt
python ../HGCTPGValidation/hgctpgvalidation/display/timing.py --reffile TimingInfo_ref.txt --testfile TimingInfo_test.txt                                                                                                                                                                                                                     
python ../HGCTPGValidation/hgctpgvalidation/display/standAloneHGCALTPGhistosCompare.py --refdir $1 --testdir $2 --webdir $3
