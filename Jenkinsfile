pipeline {
    agent {
        label 'llrgrhgtrig.in2p3.fr'
    }
    options {
        skipDefaultCheckout() 
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh '''
                uname -a
                whoami
                pwd
                ls -l
                if [ -d "./HGCTPGValidation" ] 
                then
                    rm -rf HGCTPGValidation
                fi
                git clone -b master https://github.com/ebecheva/HGCTPGValidation HGCTPGValidation
                source HGCTPGValidation/env_install.sh
                pip install attrs
                if [ -d "./test_dir" ] 
                then
                    echo "Directory test_dir exists." 
                    rm -rf test_dir
                fi
                mkdir test_dir
                cd test_dir
                pwd
                ls -lrt ..
                python ../HGCTPGValidation/scripts/validation_tpg.py --cfg HGCTPGValidation.config.user_parameters_testJenkins_cfg.py
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                echo "${env.RJPP_SCM_URL}"
                echo "${env.RJPP_JENKINSFILE}"
                echo "${env.RJPP_BRANCH}"
                sh 'true'
            }
        }
    }
}
