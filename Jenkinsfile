pipeline {
    agent {
        label 'llrgrhgtrig02.in2p3.fr'
    }
    stages {
        stage('Install - Bash script') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    withChecks('Install - Bash script') {
                        script {
                            try {
                                sh 'bash ./HGCTPGValidation/scripts/install_test.sh'
                                publishChecks title: 'Install stage',
                                              summary: 'Succeeded',
                                              conclusion: 'SUCCESS'
                            } catch (e) {
                                publishChecks title: 'Install stage',
                                              summary: "Failed: ${e.message}",
                                              conclusion: 'FAILURE'
                                throw e
                            }
                        }
                    }
                }
            }
        }

        stage('Produce - Python script') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    withChecks('Produce - Python script') {
                        script {
                            try {
                                sh 'python ./HGCTPGValidation/scripts/produce_test.py'
                                publishChecks title: 'Produce stage',
                                              summary: 'Succeeded',
                                              conclusion: 'SUCCESS'
                            } catch (e) {
                                publishChecks title: 'Produce stage',
                                              summary: "Failed: ${e.message}",
                                              conclusion: 'FAILURE'
                                throw e
                            }
                        }
                    }
                }
            }
        }
    }
}
