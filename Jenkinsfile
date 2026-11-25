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
                sh '''
                .venv/bin/python -m pytest tests/
                '''
            }
        }
    }
}
