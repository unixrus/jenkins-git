pipeline {
    agent any
    stages {
        stage('greet and capture env') {
            steps {
                sh 'echo "Hello World"'
                sh 'env'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
            }
        }
        stage('do something usefull') {
            steps {
                sh '''
                    echo "Multiline shell steps works too"
                    echo "as seen with the ls output"
                    ls -lah
                '''
            }
        }
    }
}
