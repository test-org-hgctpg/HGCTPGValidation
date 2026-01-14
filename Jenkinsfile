pipeline {
    agent {
        label 'llrgrhgtrig.in2p3.fr'
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
                echo '==> Set environment variables'
                if [ -f "log_Jenkins" ]; then
                    echo "Remove the last created log_Jenkins."
                    rm log_Jenkins
                else 
                    echo "log_Jenkins does not exist."
                fi
                } >> log_Jenkins 2> >(tee -a log_Jenkins >&2)
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
                    
                    println(env.CONFIG_SUBSET)
                    println(env.REMOTE_HGCTPGVAL)
                    println(env.BRANCH_HGCTPGVAL)
                    
                    println(env.BASE_REMOTE)
                    println(env.DATA_DIR)
                    println(env.CHANGE_TARGET)
                    println(env.CHANGE_BRANCH)
                    println(env.CHANGE_URL)
                    println(env.CHANGE_FORK)
                }
                sh '''#!/usr/bin/env bash
                {   pwd
                    ls -lrt
                    echo 'CONFIG_SUBSET=' $CONFIG_SUBSET
                    echo 'REMOTE_HGCTPGVAL=' $REMOTE_HGCTPGVAL
                    echo 'BRANCH_HGCTPGVAL=' $BRANCH_HGCTPGVAL
                    echo 'BASE_REMOTE=' $BASE_REMOTE
                    echo 'DATA_DIR=' $DATA_DIR
                    echo 'CHANGE_TARGET=' $CHANGE_TARGET
                    echo 'CHANGE_BRANCH=' $CHANGE_BRANCH
                    echo 'CHANGE_URL=' $CHANGE_URL
                    echo 'CHANGE_FORK=' $CHANGE_FORK
                } >> log_Jenkins 2> >(tee -a log_Jenkins >&2)
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
                        uname -a
                        whoami
                        if [ -d "./HGCTPGValidation" ] 
                        then
                            rm -rf HGCTPGValidation
                        fi
                        git clone -b ${BRANCH_HGCTPGVAL} https://github.com/${REMOTE_HGCTPGVAL}/HGCTPGValidation HGCTPGValidation
                        source HGCTPGValidation/env_install.sh
                        ls -lrt ..
                        } >> log_Jenkins 2> >(tee -a log_Jenkins >&2)
                        '''
                    }
                }
                stage('Clean the working environment'){
                    steps{
                        sh '''#!/usr/bin/env bash
                        {
                        set +x
                        echo 'echo ==> Clean the working environment. ============================'
                        } >> log_Jenkins 1>&2> >(tee -a log_Jenkins >&2)
                        '''
                        sh '''#!/usr/bin/env bash
                        {
                        set +x
                        echo 'echo ==> Clean the working environment. ============================'
                        ./HGCTPGValidation/scripts/clean_environment.sh ${DATA_DIR} PR$CHANGE_ID
                        mkdir test_dir
                        ls -lrt
                        } >> log_Jenkins 2> >(tee -a log_Jenkins >&2)
                        '''
                    }
                }
                stage('Set CMSSW environment variables'){
                    steps{
                        script{
                            sh '''#!/usr/bin/env bash
                            {
                            set +x
                            echo 'echo ==> Set CMSSW environment variables. ============================'
                            } >> log_Jenkins 1>&2> >(tee -a log_Jenkins >&2)
                            '''
                            try {
                                def set_var = load './HGCTPGValidation/scripts/set_CMSSW_env_variables.groovy'
                                set_var.run(env.JOB_FLAG, env.CHANGE_FORK, env.BASE_REMOTE)
                            } catch (e) {
                                echo "Error during loading or execution: ${e}"
                            }
                            println("The environment variables are:")
                            
                            echo "1 The variables are:"
                            echo "1 JOB_FLAG: ${JOB_FLAG}"
                            echo "CHANGE_BRANCH: ${CHANGE_BRANCH}"
                            echo "CHANGE_TARGET: ${CHANGE_TARGET}"
                            echo "REF_RELEASE: ${REF_RELEASE}"
                            echo "TEST_RELEASE: ${TEST_RELEASE}"
                            echo "SCRAM_ARCH: ${SCRAM_ARCH}"
                            echo "BASE_REMOTE: ${BASE_REMOTE}"
                            echo "REMOTE: ${REMOTE}"
                        }
                        sh '''#!/usr/bin/env bash
                        {
                        set +x
                        echo "The variables are:"
                        echo "JOB_FLAG: ${JOB_FLAG}"
                        echo "CHANGE_BRANCH: ${CHANGE_BRANCH}"
                        echo "CHANGE_TARGET: ${CHANGE_TARGET}"
                        echo "REF_RELEASE: ${REF_RELEASE}"
                        echo "TEST_RELEASE: ${TEST_RELEASE}"
                        echo "SCRAM_ARCH: ${SCRAM_ARCH}"
                        echo "BASE_REMOTE: ${BASE_REMOTE}"
                        echo "REMOTE: ${REMOTE}"
                        } >> log_Jenkins 2> >(tee -a log_Jenkins >&2)
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
                        srt +x
                        echo '==> Update configuration on GitHub PR comment!'
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
                                source ../../myenvPython399/bin/activate
                                module use /opt/exp_soft/vo.llr.in2p3.fr/modulefiles_el7/
                                module purge
                                module load python/3.9.9; 
                                python ../HGCTPGValidation/scripts/read_GitHubcomment.py --fileGitHub comment.tmp --fileSubset default_multi_subset.yaml
                                '''
                            ).trim()
                            if (!env.CONFIG_SUBSET_GITHUB) {
                                error("ERROR: Required environment variable CONFIG_SUBSET is not set.")
                            }else{
                                env.CONFIG_SUBSET = env.CONFIG_SUBSET_GITHUB
                                echo "CONFIG_SUBSET_GITHUB is: ${env.CONFIG_SUBSET_GITHUB}"
                                echo "CONFIG_SUBSET is set to: ${env.CONFIG_SUBSET}"
                                
                            }
                        }
                        sh '''#!/usr/bin/env bash
                        {
                        srt +x
                        echo "CONFIG_SUBSET is set to: ${CONFIG_SUBSET}"
                        } >> log_Jenkins 2> >(tee -a log_Jenkins >&2)
                        '''
                    }
                }
            }
        }
        stage('Install CMSSW Test release'){
            steps {
                sh '''#!/usr/bin/env bash
                {
                srt +x
                echo 'Install CMSSW Test release!'
                } >> log_Jenkins 1>&2> >(tee -a log_Jenkins 1>&2)
                '''
                sh '''#!/usr/bin/env bash
                {
                set +x
                echo 'echo ==> Install CMSSW Test release. ============================'
                ./HGCTPGValidation/scripts/installCMSSW_global.sh $SCRAM_ARCH $REF_RELEASE $REMOTE $BASE_REMOTE $CHANGE_BRANCH $CHANGE_TARGET ${LABEL_TEST}
                } >> log_Jenkins 2> >(tee -a log_Jenkins >&2)
                '''
            }
        }
        stage('Quality Checks'){
            steps{
                sh '''#!/usr/bin/env bash
                {
                srt +x
                echo '==> Quality Checks'
                } >> log_Jenkins 1>&2> >(tee -a log_Jenkins 1>&2)
                '''
                sh '''#!/usr/bin/env bash
                {
                set +x
                echo 'echo ==> Quality Checks. ============================'
                ./HGCTPGValidation/scripts/quality_checks.sh ${REF_RELEASE} ${LABEL_TEST}
                } >> log_Jenkins 2> >(tee -a log_Jenkins >&2)
                '''
            }
        }
        stage('Compare with CMSSW Ref Release'){
            stages{
                stage('Install Ref Release'){
                    steps {
                       sh '''#!/usr/bin/env bash
                       {
                        srt +x
                        echo ' ==> Install Ref Release'
                        } >> log_Jenkins 1>&2> >(tee -a log_Jenkins 1>&2)
                        '''
                        sh '''#!/usr/bin/env bash
                        {
                        set +x
                        echo 'echo ==> Install Ref Release. ============================'
                        ./HGCTPGValidation/scripts/installCMSSW_global.sh $SCRAM_ARCH $REF_RELEASE $BASE_REMOTE $BASE_REMOTE $CHANGE_TARGET $CHANGE_TARGET ${LABEL_REF}
                        } >> log_Jenkins 2> >(tee -a log_Jenkins >&2)
                        '''
                    }
                }
                stage('Produce Ref'){
                    steps {
                        sh '''#!/usr/bin/env bash
                        {
                        srt +x
                        echo '==> Produce reference data.'
                        } >> log_Jenkins 1>&2> >(tee -a log_Jenkins 1>&2)
                        '''
                        sh '''#!/usr/bin/env bash
                        {
                        set +x
                        echo '===> Produce reference data.'
                        cd test_dir/${REF_RELEASE}_HGCalTPGValidation_${LABEL_REF}/src
                        module use /opt/exp_soft/vo.llr.in2p3.fr/modulefiles_el7/
                        module purge
                        module load python/3.9.9
                        echo 'CONFIG_SUBSET= ' ${CONFIG_SUBSET} 
                        echo 'LABEL_TEST= ' ${LABEL_REF}
                        python ../../../HGCTPGValidation/scripts/produceData_multiconfiguration.py --subsetconfig ${CONFIG_SUBSET} --label ${LABEL_REF}
                        } >> log_Jenkins 2> >(tee -a log_Jenkins >&2)
                        '''
                    }
                }
                stage('Produce Test'){
                    steps {
                        sh '''#!/usr/bin/env bash
                        {
                        srt +x
                        echo '==> Produce test data.'
                        } >> log_Jenkins 1>&2> >(tee -a log_Jenkins 1>&2)
                        '''
                        sh '''#!/usr/bin/env bash
                        {
                        set +x
                        echo '===> Produce test data.'
                        cd test_dir/${REF_RELEASE}_HGCalTPGValidation_${LABEL_TEST}/src
                        module use /opt/exp_soft/vo.llr.in2p3.fr/modulefiles_el7/
                        module purge
                        module load python/3.9.9
                        echo 'CONFIG_SUBSET= ' ${CONFIG_SUBSET} 
                        echo 'LABEL_TEST= ' ${LABEL_TEST}
                        python ../../../HGCTPGValidation/scripts/produceData_multiconfiguration.py --subsetconfig ${CONFIG_SUBSET} --label ${LABEL_TEST}
                        } >> log_Jenkins 2> >(tee -a log_Jenkins >&2)
                        '''
                    }
                }
                stage('Display') {
                    steps {
                        sh '''#!/usr/bin/env bash
                        {
                        srt +x
                        echo '==> ==> Display'
                        } >> log_Jenkins 1>&2> >(tee -a log_Jenkins 1>&2)
                        '''
                        sh '''#!/usr/bin/env bash
                        {
                        set +x
                        echo '==> Display ======================='
                        cd test_dir
                        source ../HGCTPGValidation/env_install.sh
                        python ../HGCTPGValidation/scripts/displayHistos.py --subsetconfig ${CONFIG_SUBSET} --refdir ${REF_RELEASE}_HGCalTPGValidation_${LABEL_REF}/src --testdir ${REF_RELEASE}_HGCalTPGValidation_${LABEL_TEST}/src --datadir ${DATA_DIR} --prnumber $CHANGE_ID --prtitle "$CHANGE_TITLE (from $CHANGE_AUTHOR, $CHANGE_URL)"
                        } >> log_Jenkins 2> >(tee -a log_Jenkins >&2)
                        '''
                    }
                }
            }
        }
        stage('Geom Check') {
            steps {
                sh '''#!/usr/bin/env bash
                {
                set +x
                echo '==> Geom Check ======================='
                } >> log_Jenkins 1>&2> >(tee -a log_Jenkins >&2)
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
                    sh '''#!/usr/bin/env bash
                    {
                        ./HGCTPGValidation/scripts/write_toGitHub.sh "$url" "$MESSAGE"
                    } >> log_Jenkins 2> >(tee -a log_Jenkins >&2)
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
