import os
import sys
import attr
from attr.validators import instance_of

# Default constants 
nbrOfEvents = 50

@attr.s  
class ConfigFileParameters():
    validationRef = attr.ib(validator=instance_of(str), default='yes')
    validationTest = attr.ib(validator=instance_of(str), default='yes')
    scramArch = attr.ib(validator=instance_of(str), default='slc6_amd64_gcc700')
    releaseRefName = attr.ib(validator=instance_of(str), default='CMSSW_10_4_0_pre4')
    releaseTestName = attr.ib(validator=instance_of(str), default='CMSSW_10_4_0_pre4')
    workingRefDir = attr.ib(validator=instance_of(str), default=str(releaseRefName) +'_HGCalTPGValidation_ref')
    workingTestDir = attr.ib(validator=instance_of(str), default=str(releaseRefName) +'_HGCalTPGValidation_test')
    remoteRefBranchName = attr.ib(validator=instance_of(str), default='hgc-tpg-devel-'+str(releaseRefName))
    remoteTestBranchName = attr.ib(validator=instance_of(str), default='hgc-tpg-devel-'+str(releaseRefName))
    localRefBranchName = attr.ib(validator=instance_of(str), default='HGCalTPGValidation_ref')
    localTestBranchName = attr.ib(validator=instance_of(str), default='HGCalTPGValidation_ref')
    remoteRef = attr.ib(validator=instance_of(str), default='PFCal-dev')
    remoteTest = attr.ib(validator=instance_of(str), default='PFCal-dev')
    numberOfEvents = attr.ib(validator=instance_of(int), default=nbrOfEvents)
    conditions = attr.ib(validator=instance_of(str), default='auto:phase2_realistic')
    beamspot = attr.ib(validator=instance_of(str), default='HLLHC14TeV')
    step = attr.ib(validator=instance_of(str), default='USER:Validation/HGCalValidation/hgcalRunEmulatorValidationTPG_cff.hgcalTPGRunEmulatorValidation')
    geometryRef  = attr.ib(validator=instance_of(str), default='Extended2023D17')
    geometryTest  = attr.ib(validator=instance_of(str), default='Extended2023D17')
    eraRefName = attr.ib(validator=instance_of(str), default='Phase2')
    eraTestName = attr.ib(validator=instance_of(str), default='Phase2')
    procModifiers = attr.ib(validator=instance_of(str), default='convertHGCalDigisSim')
    inputRefFileName = attr.ib(validator=instance_of(str), default='file:/afs/cern.ch/work/j/jsauvan/public/HGCAL/TestingRelVal/CMSSW_9_3_7/RelValSingleGammaPt35/GEN-SIM-DIGI-RAW/93X_upgrade2023_realistic_v5_2023D17noPU-v2/2661406C-972C-E811-9754-0025905A60DE.root')
    inputTestFileName = attr.ib(validator=instance_of(str), default='file:/afs/cern.ch/work/j/jsauvan/public/HGCAL/TestingRelVal/CMSSW_9_3_7/RelValSingleGammaPt35/GEN-SIM-DIGI-RAW/93X_upgrade2023_realistic_v5_2023D17noPU-v2/2661406C-972C-E811-9754-0025905A60DE.root')
    customiseRefFile = attr.ib(validator=instance_of(str), default='L1Trigger/L1THGCal/customClustering.custom_2dclustering_constrainedtopological')
    customiseTestFile = attr.ib(validator=instance_of(str), default='L1Trigger/L1THGCal/customClustering.custom_2dclustering_constrainedtopological')
    dropedBranches = attr.ib(validator=instance_of(str), default='"drop l1tEMTFHit2016Extras_simEmtfDigis_CSC_HLT","drop l1tEMTFHit2016Extras_simEmtfDigis_RPC_HLT","drop l1tEMTFHit2016s_simEmtfDigis__HLT","drop l1tEMTFTrack2016Extras_simEmtfDigis__HLT","drop l1tEMTFTrack2016s_simEmtfDigis__HLT"')
    webDirPath = attr.ib(validator=instance_of(str), default='./HGCALTPG_Validation/GIFS')
    
    def installWorkingRefDir(self):
        command = 'export SCRAM_ARCH=' + self.scramArch + ';' + \
	'echo $SCRAM_ARCH'  + ';' + \
        'scramv1 p -n ' + self.workingRefDir + ' CMSSW ' + self.releaseRefName + ';' + \
        'cd ' + self.workingRefDir + '/src;' + \
        'echo $PWD; ' + \
        'eval `scramv1 runtime -sh`;' + \
        'git cms-merge-topic ' + self.remoteRef + ':' + self.remoteRefBranchName + ';' + \
        'git checkout -b ' + self.localRefBranchName + ' ' + self.remoteRef + '/' + self.remoteRefBranchName + ';' + \
        'scram b -j4; ' + 'echo === End of compilation ===;' + 'echo $PWD;' + \
        'cmsDriver.py hgcal_tpg_validation -n ' + str(self.numberOfEvents) + ' --mc  --eventcontent FEVTDEBUG --datatier GEN-SIM-DIGI-RAW --conditions ' + self.conditions + ' ' + \
        '--beamspot ' + self.beamspot + ' ' + '--step ' + self.step + ' ' + \
        '--geometry ' + self.geometryRef +  ' ' + '--era ' + self.eraRefName + ' ' + '--procModifiers ' + self.procModifiers + ' ' + \
        '--inputCommands "keep *",' + self.dropedBranches + ' ' + \
        '--filein ' + self.inputRefFileName + ' ' + \
        '--no_output ' + '--customise=' + self.customiseRefFile + ' ' + \
        '--customise_commands "process.schedule = cms.Schedule(process.user_step)" '
        return command
    
    def installWorkingTestDir(self):
        command = 'scramv1 p -n ' + self.workingTestDir + ' CMSSW ' + self.releaseTestName + ';' + \
        'cd ' + self.workingTestDir + '/src;' + \
        'echo $PWD; ' + \
        'eval `scramv1 runtime -sh`;' + \
        'git cms-merge-topic ' + self.remoteTest + ':' + self.remoteTestBranchName + ';' + \
        'git checkout -b ' + self.localTestBranchName + ' ' + self.remoteTest + '/' + self.remoteTestBranchName + ';' + \
        'scram b -j4; ' + 'echo === End of compilation ===;' + 'echo $PWD;' + \
        'cmsDriver.py hgcal_tpg_validation -n ' + str(self.numberOfEvents) + ' --mc  --eventcontent FEVTDEBUG --datatier GEN-SIM-DIGI-RAW --conditions ' + self.conditions + ' ' + \
        '--beamspot ' + self.beamspot + ' ' + '--step ' + self.step + ' ' + \
        '--geometry ' + self.geometryTest + ' ' + '--era ' + self.eraTestName + ' ' + '--procModifiers ' + self.procModifiers + ' ' + \
        '--inputCommands "keep *",' + self.dropedBranches + ' ' + \
        '--filein ' + self.inputTestFileName + ' ' + \
        '--no_output ' + '--customise=' + self.customiseTestFile + ' ' + \
        '--customise_commands "process.schedule = cms.Schedule(process.user_step)"' + ';'
        return command
