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
