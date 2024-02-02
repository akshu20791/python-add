pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                script {
                    git url: 'https://github.com/akshu20791/python-add', branch: 'master'
                }
            }
        }

     stage('Build docker image'){
            steps{
                script{
                    sh 'docker build -t simplilearn:v1 .'
                    sh 'docker images'
                }
            }
        }
      stage('Deploy') {
            steps {
               script {
                     sh 'sudo docker rm -f My-first-containe221 || true'
                     sh 'docker run -dt -p 8081:80 --name My-first-containe221 simplilearn:v1'
                  
                }
            }
        }
    }
}
