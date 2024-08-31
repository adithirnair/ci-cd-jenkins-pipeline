pipeline {
    agent any
    
    stage('Initial Test Email') {
    steps {
        emailext(
            to: 'rnairadithi05@gmail.com',
            subject: "Test Email",
            body: "This is a test email to verify email sending."
        )
    }
}


    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'No build step required'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install pytest'
            }
        }

        stage('Unit and Integration Tests') {
            steps {
                dir('src') {
                    bat 'pytest'
                }
            }
        }

        stage('Code Analysis') {
            steps {
                echo 'Code Analysis step'
            }
        }

        stage('Security Scan') {
            steps {
                echo 'Security Scan step'
            }
        }

        stage('Deploy to Staging') {
            steps {
                echo 'Deploy to Staging step'
            }
        }

        stage('Integration Tests on Staging') {
            steps {
                echo 'Integration Tests on Staging step'
            }
        }

        stage('Deploy to Production') {
            steps {
                echo 'Deploy to Production step'
            }
        }

        stage('Post Actions') {
            steps {
              emailext(
                    to: 'rnairadithi05@gmail.com',
                    subject: "Build ${currentBuild.fullDisplayName}",
                    body: "Build ${currentBuild.fullDisplayName} completed with status: ${currentBuild.currentResult}"
)

            }
            }
        }
    }

