pipeline {
    agent any

    environment {
        VENV = ".venv"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                bat '''
                python --version
                python -m venv %VENV%
                %VENV%\\Scripts\\pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                %VENV%\\Scripts\\pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                %VENV%\\Scripts\\pytest
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Python build passed'
        }
        failure {
            echo '❌ Python build failed'
        }
        always {
            cleanWs()
        }
    }
}
