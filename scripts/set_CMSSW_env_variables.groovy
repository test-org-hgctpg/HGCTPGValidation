// set_CMSSW_env_variables.groovy

// This script is used in the Jenkinsfile pipeline, in the stage 'Set CMSSW environment variables'
// Usage:
// def set_var = load './HGCTPGValidation/scripts/set_CMSSW_env_variables.groovy'
// set_var.run(env.JOB_FLAG, env.CHANGE_FORK, env.BASE_REMOTE)

def run(String JOB_FLAG, String CHANGE_FORK, String CHANGE_TARGET, String BASE_REMOTE) {
    println('Input variables in the run function')
    println("JOB_FLAG=${JOB_FLAG}")
    println("CHANGE_FORK=${CHANGE_FORK}")
    println("CHANGE_TARGET=${CHANGE_TARGET}")
    println("BASE_REMOTE=${BASE_REMOTE}")
    
    if ( JOB_FLAG == '0' ){
        env.REF_RELEASE = sh(returnStdout: true, script: 'set +x; source ./HGCTPGValidation/scripts/extractReleaseName.sh ${CHANGE_TARGET}').trim()
        env.SCRAM_ARCH = sh(returnStdout: true, script: 'set +x; source ./HGCTPGValidation/scripts/getScramArch.sh ${REF_RELEASE}').trim()
        env.TEST_RELEASE = env.REF_RELEASE
                                
        // Checks if the CHANGE_BRANCH comes from the BASE_REMMOTE or from the FORK
        if ( CHANGE_FORK ){
            env.REMOTE = CHANGE_FORK
        }
        else {
            env.REMOTE = BASE_REMOTE
        }
    }
    else {
        env.REF_BRANCH = sh(returnStdout: true, script: 'set +x; module use /opt/exp_soft/vo.llr.in2p3.fr/modulefiles_el9/; module purge; module load python/latest; python ./HGCTPGValidation/scripts/get_cmsswRefBranch.py').trim()
        env.REF_RELEASE = sh(returnStdout: true, script: 'set +x; source ./HGCTPGValidation/scripts/extractReleaseName.sh ${REF_BRANCH}').trim()
        env.SCRAM_ARCH = sh(returnStdout: true, script: 'set +x; source ./HGCTPGValidation/scripts/getScramArch.sh ${REF_RELEASE}').trim()
        env.BASE_REMOTE = sh(returnStdout: true, script: 'set +x; module use /opt/exp_soft/vo.llr.in2p3.fr/modulefiles_el9/; module purge; module load python/latest; python ./HGCTPGValidation/scripts/get_remoteParam.py').trim()
        env.CHANGE_BRANCH = env.REF_BRANCH
        env.CHANGE_TARGET = env.REF_BRANCH
        env.REMOTE = env.BASE_REMOTE
        env.TEST_RELEASE = env.REF_RELEASE
        
    }
    
    println("REF_BRANCH=${REF_BRANCH}")
    println("REF_RELEASE=${REF_RELEASE}")
    println("TEST_RELEASE=${TEST_RELEASE}")
    println("SCRAM_ARCH=${SCRAM_ARCH}")
    println("BASE_REMOTE=${BASE_REMOTE}")
    println("CHANGE_BRANCH=${CHANGE_BRANCH}")
    println("CHANGE_TARGET=${CHANGE_TARGET}")
    println("REMOTE=${REMOTE}")
}

return this
