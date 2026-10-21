pipeline {

    agent {
        label 'llrgrhgtrig02.in2p3.fr'
    }
    options {
        skipDefaultCheckout()
    }
    stages {
        stage('Install HGCTPGValidation package') {
            steps {
                withChecks('Install HGCTPGValidation package') {
                    echo 'Install HGCTPGValidation package...'
                }
            }
        }
        
        stage('Install CMSSW') {
            parallel {
                stage('Install Test') {
                    steps {
                        withChecks('Install Test') {
                            echo 'Running Install Test...'
                        }
                    }
                }
                
                stage('Install Ref') {
                    steps {
                        withChecks('Install Ref') {
                            echo 'Running install ref...'
                        }
                    }
                }
            }
        }
                
        stage('Display') {
            steps {
                withChecks('Display') {
                    echo 'Display...'
                }
            }
        }
    }
}
