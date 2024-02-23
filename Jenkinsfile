pipeline {
    triggers {
        // Trigger hook every 5 minutes
        pollSCM('H/5 * * * *')
    }
    agent {
        // Run test on the nodes with the same label
        label 'test_my_node'
    }
    parameters {
        // Add parameters for any test suite
        // booleanParam(name: 'executeTest', defaultValue: true, description: '')
        choice(
            choices: [
                'system_under_testing',
                'application_interface',
                'device_under_testing'
            ],
            description: 'My Test Suite',
            name: 'MY_SUITE'
        )
    }
    stages {
        stage('Build') {
            steps {
                echo 'Build - 1'
            }
        }
        stage('Test') {
            steps {
                echo 'Start testing - 2'
                // sh 'cd /home/pi/MY_TEST/demo/tests && python3 -m pytest -s -v -x test_system_under_testing.py'
                sh "cd /home/pi/MY_TEST/demo/tests && python3 -m pytest -s -v -x test_${params.MY_SUITE}.py"

            }
            post {
                always {
                    emailext body: 'Test result are available at : $BUILD_URL', subject: 'Test Results', to: 'omg@yahoo.com'
                }
            }
        }
    }
}