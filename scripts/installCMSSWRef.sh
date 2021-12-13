#!/bin/bash

source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc900
echo $SCRAM_ARCH
module purge
scramv1 p -n CMSSW_12_1_0_pre3_HGCalTPGValidation_ref CMSSW_12_1_0_pre3
cd CMSSW_12_1_0_pre3_HGCalTPGValidation_ref/src
echo $PWD
eval `scramv1 runtime -sh`
git config --global user.name "Emilia Becheva"
git config --global user.email emilia.becheva@llr.in2p3.fr
git cms-merge-topic ebecheva:main-dev-CMSSW_12_1_0_pre3
git checkout -b local_main-dev-CMSSW_12_1_0_pre3 ebecheva/main-dev-CMSSW_12_1_0_pre3
scram b -j8
