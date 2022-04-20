#!/bin/bash

# ./installCMSSW.sh $SCRAM_ARCH $REF_RELEASE $REMOTE $BRANCH $CHANGE_TARGET $LABEL

# $1 SCRAM_ARCH
# $2 release name
# $3 remote name 
# $4 branch name (ref or test)
# $5 branch name ref
# $6 label "ref" or "test"

export SCRAM_ARCH=$1
echo $SCRAM_ARCH
relversion=$2
echo $relversion
remote=$3
echo $remote
branch=$4
echo $branch
branch_ref=$5
echo $branch_ref
label=$6
echo $label

source /cvmfs/cms.cern.ch/cmsset_default.sh
module purge
scramv1 p -n ${relversion}_HGCalTPGValidation_$label CMSSW $relversion
cd ${relversion}_HGCalTPGValidation_$label/src
echo $PWD
eval `scramv1 runtime -sh`
git cms-merge-topic $remote:$branch
git checkout -b local_$branch $remote/$branch
git cms-merge-topic hgc-tpg:$branch_ref
scram b -j8
