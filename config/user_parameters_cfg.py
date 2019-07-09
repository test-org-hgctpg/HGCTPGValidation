import os
import sys
from HGCTPGValidation.hgctpgvalidation.parameters import ConfigFileParameters

# Install working area for reference release and/or branch and
# Generate configuration file that will simulate tpgs
generate_configFileParameters = ConfigFileParameters(
    validationRef = 'yes', #yes or no
    validationTest = 'yes', #yes or no
    scramArch = 'slc6_amd64_gcc700',
    releaseRefName = 'CMSSW_10_4_0_pre3',
    releaseTestName = 'CMSSW_10_4_0_pre3',
    workingRefDir = 'CMSSW_10_4_0_pre3_HGCalTPGValidation_ref',
    workingTestDir = 'CMSSW_10_4_0_pre3_HGCalTPGValidation_test',
    remoteRefBranchName = 'hgc-tpg-validation-CMSSW_10_4_0_pre3',
    remoteTestBranchName = 'hgc-tpg-validation-CMSSW_10_4_0_pre3',
    localRefBranchName = 'HGCalTPGValidation_ref',
    localTestBranchName = 'HGCalTPGValidation_test',
    remoteRef = 'PFCal-dev',
    remoteTest = 'PFCal-dev',
    numberOfEvents = 50,
    conditions = 'auto:phase2_realistic',
    beamspot = 'HLLHC14TeV',
    step = 'USER:Validation/HGCalValidation/hgcalRunEmulatorValidationTPG_cff.hgcalTPGRunEmulatorValidation',
    geometryRef = 'Extended2023D17',
    geometryTest = 'Extended2023D17',
    eraRefName = 'Phase2',
    eraTestName = 'Phase2',
    procModifiers = 'convertHGCalDigisSim',
    inputRefFileName = 'file:/afs/cern.ch/work/j/jsauvan/public/HGCAL/TestingRelVal/CMSSW_9_3_7/RelValSingleGammaPt35/GEN-SIM-DIGI-RAW/93X_upgrade2023_realistic_v5_2023D17noPU-v2/2661406C-972C-E811-9754-0025905A60DE.root',
    inputTestFileName = 'file:/afs/cern.ch/work/j/jsauvan/public/HGCAL/TestingRelVal/CMSSW_9_3_7/RelValSingleGammaPt35/GEN-SIM-DIGI-RAW/93X_upgrade2023_realistic_v5_2023D17noPU-v2/2661406C-972C-E811-9754-0025905A60DE.root',
    customiseRefFile = 'L1Trigger/L1THGCal/customClustering.custom_2dclustering_constrainedtopological',
    customiseTestFile = 'L1Trigger/L1THGCal/customClustering.custom_2dclustering_constrainedtopological',
    dropedBranches = '"drop l1tEMTFHit2016Extras_simEmtfDigis_CSC_HLT","drop l1tEMTFHit2016Extras_simEmtfDigis_RPC_HLT","drop l1tEMTFHit2016s_simEmtfDigis__HLT","drop l1tEMTFTrack2016Extras_simEmtfDigis__HLT","drop l1tEMTFTrack2016s_simEmtfDigis__HLT"',
    webDirPath = './GIFS_10_4_0_pre3'
    )





