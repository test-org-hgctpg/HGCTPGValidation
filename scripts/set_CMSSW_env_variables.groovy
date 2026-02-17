// set_CMSSW_env_variables.groovy

// This script is used in the Jenkinsfile pipeline, in the stage 'Set CMSSW environment variables'
// Usage:
// def set_var = load './HGCTPGValidation/scripts/set_CMSSW_env_variables.groovy'
// set_var.run(env.JOB_FLAG, env.CHANGE_FORK, env.BASE_REMOTE)

def run(String JOB_FLAG, String CHANGE_FORK, String BASE_REMOTE) {
    println('Input variables in the run function')
    println("${JOB_FLAG}")
    println("${CHANGE_FORK}")
    println("${BASE_REMOTE}")
    println("${CHANGE_TARGET}")
    if ( JOB_FLAG == '0' ){
        env.REF_RELEASE = sh(returnStdout: true, script: 'source ./HGCTPGValidation/scripts/extractReleaseName.sh ${CHANGE_TARGET}').trim()
        env.SCRAM_ARCH = sh(returnStdout: true, script: 'source ./HGCTPGValidation/scripts/getScramArch.sh ${REF_RELEASE}').trim()
        env.TEST_RELEASE = env.REF_RELEASE
        println("REF_RELEASE=${REF_RELEASE}")
        println("SCRAM_ARCH=${SCRAM_ARCH}")
        // Checks if the CHANGE_BRANCH comes from the BASE_REMMOTE or from the FORK
        if ( CHANGE_FORK ){
            println("CHANGE_FORK=${CHANGE_FORK}")
            env.REMOTE = ${CHANGE_FORK}
            println("REMOTE=${REMOTE}")
        }
        else {
            println("BASE_REMOTE=${BASE_REMOTE}")
            env.REMOTE = ${BASE_REMOTE}
        }
        println("REF_RELEASE=${REF_RELEASE}")
        println("SCRAM_ARCH=${SCRAM_ARCH}")
        println("TEST_RELEASE${TEST_RELEASE}")
        println("REMOTE=${REMOTE}")
    }
    else {
            env.REF_BRANCH = sh(returnStdout: true, script: 'set +x exec >> log_Jenkins; module use /opt/exp_soft/vo.llr.in2p3.fr/modulefiles_el7/; module purge; module load python/3.9.9; python ./HGCTPGValidation/scripts/get_cmsswRefBranch.py').trim()
            env.REF_RELEASE = sh(returnStdout: true, script: 'set +x exec >> log_Jenkins; source ./HGCTPGValidation/scripts/extractReleaseName.sh ${REF_BRANCH}').trim()
            env.SCRAM_ARCH = sh(returnStdout: true, script: 'set +x exec >> log_Jenkins; source ./HGCTPGValidation/scripts/getScramArch.sh ${REF_RELEASE}').trim()
            env.BASE_REMOTE = sh(returnStdout: true, script: 'set +x exec >> log_Jenkins; module use /opt/exp_soft/vo.llr.in2p3.fr/modulefiles_el7/; module purge; module load python/3.9.9; python ./HGCTPGValidation/scripts/get_remoteParam.py').trim()
            env.CHANGE_BRANCH = env.REF_BRANCH
            env.CHANGE_TARGET = env.REF_BRANCH
            env.REMOTE = env.BASE_REMOTE
            env.TEST_RELEASE = env.REF_RELEASE
                                
            println("${REF_BRANCH}")
            println("${REF_RELEASE}")
            println("${TEST_RELEASE}")
            println("${SCRAM_ARCH}")
            println("${BASE_REMOTE}")
            println("${CHANGE_BRANCH}")
            println("${CHANGE_TARGET}")
            println("${REMOTE}")
    }
}

return this
