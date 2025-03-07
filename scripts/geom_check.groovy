def run() {
    script{
        try{
            sh'''
            echo '===> Geometry checking.'
            
            cd test_dir/${REF_RELEASE}_HGCalTPGValidation_${LABEL_TEST}/src
            source /cvmfs/cms.cern.ch/cmsset_default.sh; 
            eval `scramv1 runtime -sh`;
            cmsRun L1Trigger/L1THGCal/test/testHGCalL1TGeometryV16_cfg.py
            '''
        } catch (e){
            echo "An error occured in Geom testing stage: ${e}"
        }
    }
}

return this
