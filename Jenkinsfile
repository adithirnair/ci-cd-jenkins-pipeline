pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                script {
                    // Print workspace files for debugging
                    bat 'dir'
                }
            }
        }
        stage('Build') {
            steps {
                echo 'No build step required'
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    bat 'python -m pip install pytest'
                }
            }
        }
        stage('Unit and Integration Tests') {
            steps {
                script {
                    // Check if pytest is available
                    bat 'python -m pip show pytest'
                    bat 'pytest'
                }
            }
        }
        stage('Code Analysis') {
            steps {
                echo 'Code Analysis skipped'
            }
        }
        stage('Security Scan') {
            steps {
                echo 'Security Scan skipped'
            }
        }
        stage('Deploy to Staging') {
            steps {
                echo 'Deploy to Staging skipped'
            }
        }
        stage('Integration Tests on Staging') {
            steps {
                echo 'Integration Tests on Staging skipped'
            }
        }
        stage('Deploy to Production') {
            steps {
                echo 'Deploy to Production skipped'
            }
        }
    }

    post {
        always {
            emailext (
                to: 'rnairadithi05@gmail.com',
                subject: "Jenkins Pipeline Result: ${currentBuild.fullDisplayName}",
                body: "The build result is: ${currentBuild.currentResult}. Check Jenkins for more details."
            )
        }
    }
}
