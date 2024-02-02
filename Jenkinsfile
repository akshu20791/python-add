pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    git url: 'https://github.com/akshu20791/python-add', branch: 'master'
                }
            }
        }

     stage('Build docker image'){
            steps{
                script{
                    sh 'docker build -t akshu20791/simplilearn:v1 .'
                    sh 'docker images'
                }
            }
        }
}
