
#!/bin/bash

source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc900
echo $SCRAM_ARCH
module purge
scramv1 p -n CMSSW_12_1_0_pre3_HGCalTPGValidation_test CMSSW_12_1_0_pre3
cd CMSSW_12_1_0_pre3_HGCalTPGValidation_test/src
echo $PWD
eval `scramv1 runtime -sh`
git cms-merge-topic ebecheva:fix-dev-CMSSW_12_1_0_pre3
git checkout -b local_main-dev-CMSSW_12_1_0_pre3 ebecheva/fix-dev-CMSSW_12_1_0_pre3
scram b -j8
