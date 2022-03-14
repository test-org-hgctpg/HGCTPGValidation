#!/bin/bash

# ./installCMSSW.sh $SCRAM_ARCH $RELEASE $CHANGE_TARGET $LABEL
# 
# $1 SCRAM_ARCH
# $2 release name
# $3 target branch name
# $4 remote remote name
# $5 label "ref" or "test"

export SCRAM_ARCH=$1
echo $SCRAM_ARCH
relversion=$2
echo $relversion
remote=$3
echo $remote
branch=$4
echo $branch
label=$5
echo $label
#echo "directory = " ${relversion}_HGCalTPGValidation_$label

source /cvmfs/cms.cern.ch/cmsset_default.sh
module purge
scramv1 p -n ${relversion}_HGCalTPGValidation_$label CMSSW $relversion
cd ${relversion}_HGCalTPGValidation_$label/src
echo $PWD
eval `scramv1 runtime -sh`
git cms-merge-topic $remote:$branch
git checkout -b local_$branch $remote/$branch
scram b -j8
