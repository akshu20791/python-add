pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Build Docker image
                    docker.build("my-python-app")
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run tests
                    docker.image('my-python-app').inside {
                        sh 'python application.py 5 7'
                    }
                }
            }
        }
    }

    post {
        always {
            // Clean up Docker images
            cleanWs()
            docker.image("my-python-app").remove()
        }
    }
}
