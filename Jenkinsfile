pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'clone the code'
                checkout scm
            }
        }

        stage('install dependencies') {
            steps {
                sh '''
                python3 -m venv .venv
                .venv/bin/python -m pip install --upgrade pip
                .venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Unit Test') {
            steps {
                echo 'test'
                withEnv([
                    'DB_HOST=127.0.0.1',
                    'DB_NAME=testdb',
                    'DB_USER=testuser',
                    'DB_PASSWORD=testpass'
                    ])
                {
                sh '''
                .venv/bin/python -m pytest tests/
                '''
                }
            }
        }
        stage('Build'){
            steps{
                sh 'docker build -t flask-notes-app:${BUILD_NUMBER} .'
            }
        }
        stage('image scan'){
            steps{
                sh '''
                  trivy --config "" image \
                  --severity HIGH,CRITICAL \
                  --exit-code 0 \
                  flask-notes-app:${BUILD_NUMBER}
                  '''
            }
        }
        stage("push image to docker hub"){
                steps{
                    withCredentials([usernamePassword(
                    credentialsId:"dockerHubcred",
                    usernameVariable:"dockerHubUser", 
                    passwordVariable:"dockerHubPass")]){
                sh 'echo $dockerHubPass | docker login -u $dockerHubUser --password-stdin'
                sh "docker image tag flask-notes-app:${BUILD_NUMBER} ${env.dockerHubUser}/flask-notes-app:${BUILD_NUMBER}"
                sh "docker push ${env.dockerHubUser}/flask-notes-app:${BUILD_NUMBER}"
                }
                }
                
            }
        stage('Deployment'){
            steps{
                sh'''
                docker pull ${env.dockerHubUser}/flask-notes-app:${BUILD_NUMBER}
                docker rm -f flask-deployment || true
                docker run -d \
                -- name flask-deployment \
                -- network flask-deployment-net \
                -e DB_HOST=jenkins-test-db \
                -e DB_NAME=testdb \
                -e DB_USER=$DB_USER \
                -e DB_PASSWORD=$DB_PASSWORD \
                $env.dockerHubUser/flask-notes-app:$BUILD_NUMBER
                }
                '''
            }
        }
                
    }
}
