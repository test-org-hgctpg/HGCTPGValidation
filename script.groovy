def runcmsDriver(){
    cmsDriver.py hgcal_tpg_validation -n 50 + \
    --mc --eventcontent FEVTDEBUG --datatier GEN-SIM-DIGI-RAW + \
    --conditions auto:phase2_realistic + \
    --beamspot HLLHC14TeV + \
    --step USER:Validation/HGCalValidation/hgcalRunEmulatorValidationTPG_cff.hgcalTPGRunEmulatorValidation + \
    --geometry Extended2026D49 + \
    --era Phase2C9 + \
    --procModifiers '' + \
    --inputCommands "keep *", "drop l1tEMTFHit2016Extras_simEmtfDigis_CSC_HLT","drop l1tEMTFHit2016Extras_simEmtfDigis_RPC_HLT","drop l1tEMTFHit2016s_simEmtfDigis__HLT","drop l1tEMTFTrack2016Extras_simEmtfDigis__HLT","drop l1tEMTFTrack2016s_simEmtfDigis__HLT" + \
    --filein file:/data_CMS_upgrade/becheva/data_jenkins/003F2BA9-0D02-5A43-A53F-4161E513BFA6.root + \
    --no_output --customise=L1Trigger/L1THGCal/customClustering.custom_2dclustering_constrainedtopological + \
    --customise_commands "process.MessageLogger.files.out_ref = dict()\n process.Timing = cms.Service('Timing', summaryOnly = cms.untracked.bool(False), useJobReport = cms.untracked.bool(True))\n process.SimpleMemoryCheck = cms.Service('SimpleMemoryCheck', ignoreTotal = cms.untracked.int32(1))\n process.schedule = cms.Schedule(process.user_step)"
}

return this
