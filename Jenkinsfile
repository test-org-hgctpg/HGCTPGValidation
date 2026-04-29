pipeline {
    agent {
        label 'llrgrhgtrig02.in2p3.fr'
    }
    environment {
        LABEL_TEST='test'
        LABEL_REF='ref'
    }
    options {
        skipDefaultCheckout()
        buildDiscarder logRotator(artifactDaysToKeepStr: '7', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '')
    }
    stages {
        stage('Set environment variables'){
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
                
                echo '==> Set environment variables. ============================'
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
                            env.BRANCH_HGCTPGVAL='Jenkins-feature-modularJenkinsfile'
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
        stage('Initialize'){
            stages{
                stage('Install automatic validation package HGCTPGValidation') {
                    steps {
                        sh '''#!/usr/bin/env bash
                        {
                        set +x
                        echo '==> Install automatic validation package HGCTPGValidation. ============================'
                        echo 'Cloning the branch ' ${BRANCH_HGCTPGVAL} ' from https://github.com/'${REMOTE_HGCTPGVAL}'/HGCTPGValidation'
                        } >> log_Jenkins 1>&2> >(tee -a log_Jenkins >&2)
                        '''
                        sh '''#!/usr/bin/env bash
                        {
                        set +x
                        if [ -d "./HGCTPGValidation" ] 
                        then
                            rm -rf HGCTPGValidation
                        fi
                        git clone -b ${BRANCH_HGCTPGVAL} https://github.com/${REMOTE_HGCTPGVAL}/HGCTPGValidation HGCTPGValidation
                        source HGCTPGValidation/env_install.sh
                        } >> log_Jenkins 2> >(tee -a log_Jenkins >&2)
                        '''
                    }
                }
                stage('Clean the working environment'){
                    steps{
                        sh '''#!/usr/bin/env bash
                        set +x
                        echo 'echo ==> Clean the working environment. ============================'
                        ./HGCTPGValidation/scripts/clean_environment.sh ${DATA_DIR} PR$CHANGE_ID
                        mkdir test_dir
                        } >> log_Jenkins 1>&2> >(tee -a log_Jenkins >&2)
                        '''
                    }
                }
                stage('Set CMSSW environment variables'){
                    steps{
                        script{
                            sh '''#!/usr/bin/env bash
                            set +x
                            echo 'echo ==> Set CMSSW environment variables. ============================'
                            } >> log_Jenkins 1>&2> >(tee -a log_Jenkins >&2)
                            '''
                            try {
                                def set_var = load './HGCTPGValidation/scripts/set_CMSSW_env_variables.groovy'
                                set_var.run(env.JOB_FLAG, env.CHANGE_FORK, env.CHANGE_TARGET, env.BASE_REMOTE)
                            } catch (e) {
                                echo "Error during loading or execution: ${e}"
                            }
                        }
                        sh '''#!/usr/bin/env bash
                        {
                        set +x
                        echo "The environment variables are:"
                        echo "JOB_FLAG: ${JOB_FLAG}"
                        echo "CHANGE_BRANCH: ${CHANGE_BRANCH}"
                        echo "CHANGE_TARGET: ${CHANGE_TARGET}"
                        echo "REF_RELEASE: ${REF_RELEASE}"
                        echo "TEST_RELEASE: ${TEST_RELEASE}"
                        echo "SCRAM_ARCH: ${SCRAM_ARCH}"
                        echo "BASE_REMOTE: ${BASE_REMOTE}"
                        echo "REMOTE: ${REMOTE}"
                        } >> log_Jenkins 1>&2> >(tee -a log_Jenkins >&2)
                        '''
                    }
                }
                stage('Set config files for specific release'){
                    steps{
                    sh '''#!/usr/bin/env bash
                    {
                    set +x
                    echo '===> Set config files for specific release.'
                    
                    ./HGCTPGValidation/scripts/remove_outerr.sh
                    
                    } >> log_Jenkins 1>&2> >(tee -a log_Jenkins >&2)
                    '''
                    sh '''#!/usr/bin/env bash
                    {
                    set +x
                    cd test_dir
                    source ../HGCTPGValidation/env_install.sh
                    python ../HGCTPGValidation/scripts/split_configFiles.py --releaseName ${REF_RELEASE}
                    statusSplitConfigFiles=$?
                    } >> log_Jenkins 2> >(tee -a log_Jenkins out_err)
                    
                    # If the script split_configFiles.py fails, the pipeline stops
                     ../HGCTPGValidation/scripts/check_command_status.sh $statusSplitConfigFiles $STAGE_NAME
                    '''
                    }
                }
                stage('Update the configuration'){
                    when {
                        expression {
                            // Only run this stage if the build was triggered by a PR comment that contains new customise parameter
                            def causes = currentBuild.getBuildCauses('com.adobe.jenkins.github_pr_comment_build.GitHubPullRequestCommentCause')
                            return causes && (causes[0].commentBody?.contains("Jenkins") && causes[0].commentBody?.contains("test"))
                        }
                    }
                    steps {
                        sh '''#!/usr/bin/env bash
                        {
                        set +x
                        echo '==> Update configuration on GitHub PR comment! ================================='
                        } >> log_Jenkins 1>&2> >(tee -a log_Jenkins 1>&2)
                        '''
                        script{
                            // Comments
                            def commentCauses = currentBuild.getBuildCauses('com.adobe.jenkins.github_pr_comment_build.GitHubPullRequestCommentCause')
                            if (commentCauses) {
                                for (def commentCause : commentCauses) {
                                    echo("""Comment Author: ${commentCause.commentAuthor}, Body: "${commentCause.commentBody}" (${commentCause.commentUrl})""")
                                    def comment = commentCauses[0].commentBody
                                    writeFile file: 'comment.tmp', text: comment
                                    env.COMMENT=comment
                                    echo "PR Comment: ${comment}"
                                }
                            } else {
                                echo("Build was not started by a PR comment")
                            }
                            env.CONFIG_SUBSET_GITHUB = sh(
                            returnStdout: true,
                            script: '''
                                set +x
                                cd test_dir
                                source ../HGCTPGValidation/env_install.sh
                                python ../HGCTPGValidation/scripts/read_GitHubcomment.py --fileGitHub comment.tmp --fileSubset default_multi_subset.yaml
                                '''
                            ).trim()
                            if (!env.CONFIG_SUBSET_GITHUB) {
                                error("ERROR: Required environment variable CONFIG_SUBSET is not set.")
                            }else{
                                env.CONFIG_SUBSET = env.CONFIG_SUBSET_GITHUB
                                echo "CONFIG_SUBSET is set to: ${env.CONFIG_SUBSET_GITHUB}"
                            }
                        }
                        sh '''#!/usr/bin/env bash
                        {
                        set +x
                        echo "PR Comment: ${GITHUB_COMMENT}"
                        echo "CONFIG_SUBSET is set to: ${CONFIG_SUBSET}"
                        } >> log_Jenkins 1>&2> >(tee -a log_Jenkins 1>&2)
                        '''
                    }
                }
            }
        }
        stage('Install CMSSW Test release'){
            steps {
                sh '''#!/usr/bin/env bash
                {
                set +x
                echo '==> Install CMSSW Test release. ============================'
                
                ./HGCTPGValidation/scripts/remove_outerr.sh
                
                } >> log_Jenkins 1>&2> >(tee -a log_Jenkins 1>&2)
                '''
                sh '''#!/usr/bin/env bash
                {
                set +x
                ./HGCTPGValidation/scripts/installCMSSW_global.sh $SCRAM_ARCH $REF_RELEASE $REMOTE $BASE_REMOTE $CHANGE_BRANCH $CHANGE_TARGET ${LABEL_TEST}
                statusInstallTest=$?
                } >> log_Jenkins 2> >(tee -a log_Jenkins out_err) # the std_err is redirected to log_Jenkins and to out_err
                
                # If the script installCMSSW_global.sh fails, the pipeline stops
                ../HGCTPGValidation/scripts/check_command_status.sh $statusInstallTest $STAGE_NAME
                '''
            }
        }
        stage('Quality Checks'){
            steps{
                sh '''#!/usr/bin/env bash
                {
                set +x
                echo 'echo ==> Quality Checks. ============================'
                
                ./HGCTPGValidation/scripts/remove_outerr.sh
                
                } >> log_Jenkins 1>&2> >(tee -a log_Jenkins 1>&2)
                '''
                sh '''#!/usr/bin/env bash
                {
                set +x
                ./HGCTPGValidation/scripts/quality_checks.sh ${REF_RELEASE} ${LABEL_TEST}
                statusQualityChecks=$?
                } >> log_Jenkins 2> >(tee -a log_Jenkins out_err)
                
                # If the script quality_checks.sh fails, the pipeline stops
                ../HGCTPGValidation/scripts/check_command_status.sh $statusQualityChecks $STAGE_NAME
                '''
            }
        }
        stage('Compare with CMSSW Ref Release'){
            stages{
                stage('Install Ref Release'){
                    steps {
                        sh '''
                        set +x
                        echo 'echo ==> Install Ref Release. ============================'
                        exec >> log_Jenkins
                        echo 'echo ==> Install Ref Release. ============================'
                        ./HGCTPGValidation/scripts/installCMSSW_global.sh $SCRAM_ARCH $REF_RELEASE $BASE_REMOTE $BASE_REMOTE $CHANGE_TARGET $CHANGE_TARGET ${LABEL_REF}
                        echo '      '
                        '''
                    }
                }
                stage('Produce Ref'){
                    steps {
                        sh '''
                        set +x
                        echo '===> Produce reference data.'
                        exec >> log_Jenkins
                        echo '===> Produce reference data.'
                        pwd
                        cd test_dir/${REF_RELEASE}_HGCalTPGValidation_${LABEL_REF}/src
                        source ../../../HGCTPGValidation/env_install.sh
                        python ../../../HGCTPGValidation/scripts/produceData_multiconfiguration.py --subsetconfig ${CONFIG_SUBSET} --label ${LABEL_REF}
                        echo '      '
                        '''
                    }
                }
                stage('Produce Test'){
                    steps {
                        sh '''
                        set +x
                        echo '===> Produce test data.'
                        exec >> log_Jenkins
                        echo '===> Produce test data.'
                        cd test_dir/${REF_RELEASE}_HGCalTPGValidation_${LABEL_TEST}/src
                        source ../../../HGCTPGValidation/env_install.sh
                        python ../../../HGCTPGValidation/scripts/produceData_multiconfiguration.py --subsetconfig ${CONFIG_SUBSET} --label ${LABEL_TEST}
                        echo '      '
                        '''
                    }
                }
                stage('Display') {
                    steps {
                        sh '''
                        set +x
                        echo '==> Display ======================='
                        exec >> log_Jenkins
                        echo '==> Display ======================='
                        cd test_dir
                        source ../HGCTPGValidation/env_install.sh
                        python ../HGCTPGValidation/scripts/displayHistos.py --subsetconfig ${CONFIG_SUBSET} --refdir ${REF_RELEASE}_HGCalTPGValidation_${LABEL_REF}/src --testdir ${REF_RELEASE}_HGCalTPGValidation_${LABEL_TEST}/src --datadir ${DATA_DIR} --prnumber $CHANGE_ID --prtitle "$CHANGE_TITLE (from $CHANGE_AUTHOR, $CHANGE_URL)"
                        echo '      '
                        '''
                    }
                }
            }
        }
        stage('Geom Check') {
            steps {
                sh '''
                set +x
                echo '==> Geom Check ======================='
                exec >> log_Jenkins
                echo '==> Geom Check ======================='
                '''
                script{
                    try{
                        sh'./HGCTPGValidation/scripts/geom_check.sh ${TEST_RELEASE} ${LABEL_TEST}'
                    } catch (e){
                        error("An error occured in Geom testing stage: ${e}")
                    }
                }
            }
        }
    }
    post {
        always {
            script{
                if ( env.JOB_FLAG=='1' ) {    
                    env.CHANGE_BRANCH = env.BRANCH_HGCTPGVAL
                    env.CHANGE_TARGET = env.CHANGE_TARGET_HGCTPGVAL
                    println( "Validation of the validation: Set the original name of CHANGE_BRANCH => " + env.CHANGE_BRANCH )
                }
                
                def message = ""
                if (currentBuild.result == 'SUCCESS') {
                    message = "The validation checks have passed." + "<br>" + "The comparison histograms are available [here](${env.WEBPAGES_VAL}list_config.php?pr=/PR$CHANGE_ID)"
                } else if (currentBuild.result == 'FAILURE') {
                    message = "Some of the validation checks have failed." + "<br>" + "More details can be found [here](${env.CHANGE_URL}/checks)"
                
                }
                
                withEnv(["MESSAGE=${message}","url=${env.CHANGE_URL}"]) {
                    // Generate a token, the command "set +x" is mandatory
                    sh '''
                        ./HGCTPGValidation/scripts/write_toGitHub.sh "$url" "$MESSAGE"
                    '''
                }
            }
            archiveArtifacts artifacts: 'log_Jenkins, test_dir/**/src/test_triggergeom.root', fingerprint: true
        }
        success {
            echo 'The job finished successfully.'
            mail to: "${EMAIL_TO}",
                 subject: "Jenkins job succeded: ${currentBuild.fullDisplayName}",
                 body:  "The job finished successfully. \n\n Pull request: ${env.BRANCH_NAME} build number: #${env.BUILD_NUMBER} \n\n Title: ${env.CHANGE_TITLE} \n\n Author of the PR: ${env.CHANGE_AUTHOR} \n\n Target branch: ${env.CHANGE_TARGET} \n\n Feature branch: ${env.CHANGE_BRANCH} \n\n Check console output at ${env.BUILD_URL} \n\n and ${env.CHANGE_URL} to view the results.  \n\n The validation histograms are available at ${env.WEBPAGES_VAL}list_config.php?pr=/PR$CHANGE_ID \n\n"
        }
        failure {
            echo 'Job failed'
            mail to: "${EMAIL_TO}",
                 subject: "Jenkins job failed: ${currentBuild.fullDisplayName}",
                 body: "The compilation or the build steps failed. \n\n Pull request: ${env.BRANCH_NAME} build number: #${env.BUILD_NUMBER} \n\n Title: ${env.CHANGE_TITLE} \n\n Author of the PR: ${env.CHANGE_AUTHOR} \n\n Target branch: ${env.CHANGE_TARGET} \n\n Feature branch: ${env.CHANGE_BRANCH} \n\n Check console output at ${env.BUILD_URL} \n\n and ${env.CHANGE_URL} to view the results.  \n\n The validation histograms are available at ${env.WEBPAGES_VAL} \n\n"
        }
    }
}
