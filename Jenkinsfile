pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('List Workspace Files') {
            steps {
                script {
                    bat 'dir'
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    // Adjust this if you have a different setup
                    echo 'No build step required'
                }
            }
        }
        stage('Unit and Integration Tests') {
            steps {
                script {
                    // Example: Run tests using pytest
                    bat 'pytest'
                }
            }
        }
        stage('Code Analysis') {
            steps {
                script {
                    // Example: Run static code analysis using pylint
                    bat 'pylint main.py'
                }
            }
        }
        stage('Security Scan') {
            steps {
                script {
                    // Example: Run security scan (replace with actual tool and command)
                    bat 'bandit -r main.py'
                }
            }
        }
        stage('Deploy to Staging') {
            steps {
                script {
                    // Example: Deployment step (adjust as needed)
                    echo 'Deploying to staging...'
                }
            }
        }
        stage('Integration Tests on Staging') {
            steps {
                script {
                    // Example: Run integration tests on staging (if applicable)
                    echo 'Running integration tests on staging...'
                }
            }
        }
        stage('Deploy to Production') {
            steps {
                script {
                    // Example: Deployment step (adjust as needed)
                    echo 'Deploying to production...'
                }
            }
        }
    }

    post {
        always {
            emailext(
                subject: "Pipeline ${currentBuild.fullDisplayName}",
                body: "The pipeline ${currentBuild.fullDisplayName} has finished. Check the Jenkins console output for details.",
                to: 'rnairadithi05@gmail.com'
            )
        }
    }
}

