pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                script {
                    // Example: Install dependencies if you have a requirements.txt
                    bat 'pip install -r requirements.txt'
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

