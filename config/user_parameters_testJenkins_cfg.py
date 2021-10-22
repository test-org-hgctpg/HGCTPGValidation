import os
import sys
from HGCTPGValidation.hgctpgvalidation.parameters import ConfigFileParameters

# Install working area for reference release and/or branch and
# Generate configuration file that will simulate tpgs
generate_configFileParameters = ConfigFileParameters(
    validationRef = True, #True or False
    validationTest = True, #True or False
    installStep = True, #True or False
    compileStep = True, #True or False
    simulationStep = True, #True or False
    scramArch = 'slc7_amd64_gcc900',
    releaseRefName = 'CMSSW_12_1_0_pre3',
    releaseTestName = 'CMSSW_12_1_0_pre3',
    workingRefDir = 'CMSSW_12_1_0_pre3_HGCalTPGValidation_ref',
    workingTestDir = 'CMSSW_12_1_0_pre3_HGCalTPGValidation_test',
#    remoteRefBranchName = 'hgc-tpg-devel-CMSSW_12_1_0_pre3',
#    remoteTestBranchName = 'hgc-tpg-devel-CMSSW_12_1_0_pre3',
#    localRefBranchName = 'local_hgc-tpg-devel-CMSSW_12_1_0_pre3',
#    localTestBranchName = 'local_hgc-tpg-devel-CMSSW_12_1_0_pre3',
    remoteRefBranchName = 'main-dev-CMSSW_12_1_0_pre3',
    remoteTestBranchName = 'fix-dev-CMSSW_12_1_0_pre3',
    localRefBranchName = 'local_main-dev-CMSSW_12_1_0_pre3',
    localTestBranchName = 'local_main-dev-CMSSW_12_1_0_pre3',
#    remoteRef = 'PFCal-dev',
#    remoteTest = 'PFCal-dev',
    remoteRef = 'ebecheva',
    remoteTest = 'ebecheva',
    numberOfEvents = 50,
    conditions = 'auto:phase2_realistic',
    beamspot = 'HLLHC14TeV',
    step = 'USER:Validation/HGCalValidation/hgcalRunEmulatorValidationTPG_cff.hgcalTPGRunEmulatorValidation',
    geometryRef = 'Extended2026D49',
    geometryTest = 'Extended2026D49',
    eraRefName = 'Phase2C9',
    eraTestName = 'Phase2C9',
    procModifiers = '',
#    inputRefFileName = '/data_cms_upgrade/sauvan/HGCAL/DIGI/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/2D0339A5-751F-3543-BA5B-456EA6E5E294.root',
#    inputTestFileName = '/data_cms_upgrade/sauvan/HGCAL/DIGI/Phase2HLTTDRWinter20DIGI/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/2D0339A5-751F-3543-BA5B-456EA6E5E294.root',
    inputRefFileName = 'root://cms-xrd-global.cern.ch///eos/cms//store/mc/Phase2HLTTDRWinter20DIGI/QCD_Pt-15to7000_TuneCP5_Flat_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0To200_castor_110X_mcRun4_realistic_v3_ext1-v1/260000/003F2BA9-0D02-5A43-A53F-4161E513BFA6.root',
    inputTestFileName = 'root://cms-xrd-global.cern.ch///eos/cms//store/mc/Phase2HLTTDRWinter20DIGI/QCD_Pt-15to7000_TuneCP5_Flat_14TeV-pythia8/GEN-SIM-DIGI-RAW/FlatPU0To200_castor_110X_mcRun4_realistic_v3_ext1-v1/260000/003F2BA9-0D02-5A43-A53F-4161E513BFA6.root',
    #customiseRefFile = 'L1Trigger/L1THGCal/customClustering.custom_2dclustering_constrainedtopological',
    #customiseTestFile = 'L1Trigger/L1THGCal/customClustering.custom_2dclustering_constrainedtopological',
    customiseRefFile = '',
    customiseTestFile = '',
    dropedBranches = '"drop l1tEMTFHit2016Extras_simEmtfDigis_CSC_HLT","drop l1tEMTFHit2016Extras_simEmtfDigis_RPC_HLT","drop l1tEMTFHit2016s_simEmtfDigis__HLT","drop l1tEMTFTrack2016Extras_simEmtfDigis__HLT","drop l1tEMTFTrack2016s_simEmtfDigis__HLT"',
    webDirPath = './GIFS'
    )
