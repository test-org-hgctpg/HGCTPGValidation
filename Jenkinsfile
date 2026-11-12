def checked(String name, String cmd) {
    def logFile = "${name.replaceAll('[^A-Za-z0-9]', '_')}.log"
    def rc = -1
    def failed = false

    publishChecks name: name, status: 'IN_PROGRESS',
                  title: name, summary: 'Running...'
    try {
        rc = sh(script: "${cmd} > ${logFile} 2>&1", returnStatus: true)
        def output = readFile(logFile).trim()
        echo output
        if (output.length() > 2000) {
            output = output.substring(output.length() - 2000)
        }

        if (rc == 0) {
            publishChecks name: name, title: name,
                          summary: 'Succeeded', conclusion: 'SUCCESS'
        } else {
            publishChecks name: name, title: name,
                          summary: "Failed with exit code ${rc}",
                          text: '```\n' + output + '\n```',
                          conclusion: 'FAILURE'
            failed = true
        }
    } catch (org.jenkinsci.plugins.workflow.steps.FlowInterruptedException e) {
        publishChecks name: name, title: name,
                      summary: 'Aborted', conclusion: 'CANCELED'
        throw e
    } catch (e) {
        publishChecks name: name, title: name,
                      summary: "Unexpected error: ${e.message}", conclusion: 'FAILURE'
        throw e
    }

    if (failed) {
        error("${name} failed with exit code ${rc}")
    }
}

pipeline {
    agent {
        label 'llrgrhgtrig02.in2p3.fr'
    }
    options {
        skipDefaultCheckout()
    }
    
    stages {
        stage('Set_environment_variables'){
            steps{
                sh '''#!/usr/bin/env bash
                {
                set +x
                if [ -f "log_Jenkins" ]; then
                    echo "Remove the last created log_Jenkins."
                    rm log_Jenkins
                else
                    echo "log_Jenkins does not exist."
                fi
                
                echo '\n==> Set environment variables ============================'
                } >> log_Jenkins 1>&2> >(tee -a log_Jenkins >&2)
                '''
                script{
                    String s = env.JOB_NAME
                    String[] elements = s.split("/")
                    String job_name = elements[-2]
                    println(job_name);
                    switch(job_name){
                       case 'HGC TPG CMSSW Validation':
                            env.EMAIL_TO=env.HGCTPG_EMAIL_TO_MAIN
                            env.BASE_REMOTE=env.HGCTPG_BASE_REMOTE_MAIN
                            env.REMOTE_HGCTPGVAL=env.BASE_REMOTE
                            env.DATA_DIR=env.HGCTPG_DATA_DIR_MAIN
                            env.BRANCH_HGCTPGVAL=env.HGCTPG_BRANCH_VAL_MAIN
                            env.WEBPAGES_VAL=env.HGCTPG_WEBPAGES_VAL_CMSSW_PROD
                            env.JOB_FLAG=0
                            break
                        case 'HGC TPG Automatic Validation - TEST':
                            env.EMAIL_TO=env.HGCTPG_EMAIL_TO_EB
                            env.BASE_REMOTE=env.HGCTPG_BASE_REMOTE_TEST
                            env.REMOTE_HGCTPGVAL=env.BASE_REMOTE
                            env.DATA_DIR=env.HGCTPG_DATA_DIR_TEST
                            env.BRANCH_HGCTPGVAL=env.HGCTPG_BRANCH_VAL_TEST
                            env.WEBPAGES_VAL=env.HGCTPG_WEBPAGES_VAL_CMSSW_TEST
                            env.JOB_FLAG=0
                            break
                        case 'HGC TPG Automatic Validation - TEST ebecheva':
                            env.EMAIL_TO=env.HGCTPG_EMAIL_TO_EB
                            env.BASE_REMOTE=env.HGCTPG_BASE_REMOTE_EB
                            env.REMOTE_HGCTPGVAL=env.BASE_REMOTE
                            env.DATA_DIR=env.HGCTPG_DATA_DIR_EB
                            env.BRANCH_HGCTPGVAL=env.HGCTPG_BRANCH_VAL_EB
                            env.WEBPAGES_VAL=env.HGCTPG_WEBPAGES_VAL_CMSSW_TEST_EB
                            env.JOB_FLAG=0
                            break
                        case 'HGC TPG Automatic Validation - TEST jbsauvan':
                            env.EMAIL_TO=env.HGCTPG_EMAIL_TO_JB
                            env.BASE_REMOTE=env.HGCTPG_BASE_REMOTE_JB
                            env.REMOTE_HGCTPGVAL=env.BASE_REMOTE
                            env.DATA_DIR=env.HGCTPG_DATA_DIR_JB
                            env.BRANCH_HGCTPGVAL=env.HGCTPG_BRANCH_VAL_JB
                            env.WEBPAGES_VAL=env.HGCTPG_WEBPAGES_VAL_CMSSW_TEST_JB
                            env.JOB_FLAG=0
                            break
                        case 'HGC TPG Validation Validation':
                            env.EMAIL_TO=env.HGCTPG_EMAIL_TO_MAIN
                            env.BASE_REMOTE=env.HGCTPG_BASE_REMOTE_MAIN
                            env.DATA_DIR=env.HGCTPG_DATA_DIR_VALTEST
                            env.WEBPAGES_VAL=env.HGCTPG_WEBPAGES_VAL_CODE_TEST
                            env.JOB_FLAG=1
                            break
                        case 'HGC TPG Dev Validation - ebecheva':
                            env.EMAIL_TO=env.HGCTPG_EMAIL_TO_EB
                            env.BASE_REMOTE=env.HGCTPG_BASE_REMOTE_EB
                            env.DATA_DIR=env.HGCTPG_DATA_DIR_EB
                            env.WEBPAGES_VAL=env.HGCTPG_WEBPAGES_VAL_CMSSW_TEST_EB
                            env.JOB_FLAG=1
                            break
                        case 'HGC TPG Validation - org':
                            env.EMAIL_TO=env.HGCTPG_EMAIL_TO_EB
                            env.BASE_REMOTE=env.HGCTPG_BASE_REMOTE_EB_org
                            env.DATA_DIR=env.HGCTPG_DATA_DIR_EB
                            env.WEBPAGES_VAL=env.HGCTPG_WEBPAGES_VAL_CMSSW_TEST_EB
                            env.JOB_FLAG=1
                            break
                        case 'CMSSW Dev Validation - org':
                            env.EMAIL_TO=env.HGCTPG_EMAIL_TO_EB
                            env.BASE_REMOTE=env.HGCTPG_BASE_REMOTE_EB_org
                            env.REMOTE_HGCTPGVAL=env.BASE_REMOTE
                            env.DATA_DIR=env.HGCTPG_DATA_DIR_EB
                            env.BRANCH_HGCTPGVAL=env.HGCTPG_BRANCH_VAL_EB_ORG
                            env.WEBPAGES_VAL=env.HGCTPG_WEBPAGES_VAL_CMSSW_TEST_EB
                            env.JOB_FLAG=0
                            break
                        default: 
                            println("The job name is unknown"); 
                            break
                    }
                    
                    if (env.JOB_FLAG=='1'){
                        
                        env.BRANCH_HGCTPGVAL=env.CHANGE_BRANCH
                        env.CHANGE_TARGET_HGCTPGVAL=env.CHANGE_TARGET
                        
                        if (env.CHANGE_FORK){
                            env.REMOTE_HGCTPGVAL = env.CHANGE_FORK
                        }
                        else {
                            env.REMOTE_HGCTPGVAL = env.BASE_REMOTE
                        }
                    }
                    env.CONFIG_SUBSET = 'default_multi_subset'
                }
                sh '''#!/usr/bin/env bash
                {   pwd
                    echo 'JOB_NAME=' $JOB_NAME
                    echo 'JOB_FLAG=' $JOB_FLAG
                    echo 'CHANGE_URL=' $CHANGE_URL
                    echo 'CHANGE_FORK=' $CHANGE_FORK
                    echo 'CHANGE_BRANCH=' $CHANGE_BRANCH
                    echo 'CHANGE_TARGET=' $CHANGE_TARGET
                    echo 'CONFIG_SUBSET=' $CONFIG_SUBSET
                    echo 'REMOTE_HGCTPGVAL=' $REMOTE_HGCTPGVAL
                    echo 'BRANCH_HGCTPGVAL=' $BRANCH_HGCTPGVAL
                    echo 'BASE_REMOTE=' $BASE_REMOTE
                    echo 'DATA_DIR=' $DATA_DIR
                    echo 'EMAIL_TO=' $EMAIL_TO
                    echo 'WEBPAGES_VAL=' $WEBPAGES_VAL
                } >> log_Jenkins 1>&2> >(tee -a log_Jenkins >&2)
                '''
            }  
        }
        stage('Install_automatic_validation_package_HGCTPGValidation') {
            steps {
                sh '''#!/usr/bin/env bash
                {
                set +x
                if [ -d "./HGCTPGValidation" ] 
                then
                    echo "Remove previsous HGCTPGValidation package."
                    rm -rf HGCTPGValidation
                fi
                ls -lrt
                pwd
                git clone -b ${BRANCH_HGCTPGVAL} https://github.com/${REMOTE_HGCTPGVAL}/HGCTPGValidation HGCTPGValidation
                ls -lrt
                source HGCTPGValidation/env_install.sh
                } 
                '''
            }
        }
        stage('Install test - Bash script') {
            steps {
                checked('Install test - Bash script', 'bash ./HGCTPGValidation/scripts/install_test.sh')
            }
        }
        stage('Quality checks - Bash script') {
            steps {
                checked('Quality checks - Bash script', 'bash ./HGCTPGValidation/scripts/quality_testing.sh')
            }
        }
        stage('Parallel tasks'){
            parallel{
                stage('Reference part'){
                    stages{
                        stage('Install ref - Bash script') {
                            steps {
                                checked('Install ref - Bash script', 'bash ./HGCTPGValidation/scripts/install_test.sh')
                            }
                        }
                        stage('Produce ref - Python script') {
                            steps {
                                checked('Produce ref - Python script', 'python ./HGCTPGValidation/scripts/produce_ref.py')
                            }
                        }
                    }
                }
                stage('Produce test - Python script') {
                    steps {
                        checked('Produce test - Python script', 'python ./HGCTPGValidation/scripts/produce_test.py')
                    }
                }
                stage('Geom check - Bash script') {
                    steps {
                        catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                            checked('Geom check - Bash script', 'bash ./HGCTPGValidation/scripts/geom_check_testing.sh')
                        }
                    }
                }
            }
        }
        stage('Display - Python script') {
            steps {
                checked('Display - Python script', 'python ./HGCTPGValidation/scripts/display_testing.py')
            }
        }
    }
}
