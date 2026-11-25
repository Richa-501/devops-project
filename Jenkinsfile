pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'clone the code'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building Flask application'
            }
        }

        stage('Test') {
            steps {
                echo 'Running application tests'
            }
        }
    }
}
