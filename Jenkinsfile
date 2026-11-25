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
                  --exit-code 1 \
                  flask-notes-app:${BUILD_NUMBER}
                  '''
            }
        }
                
    }
}
