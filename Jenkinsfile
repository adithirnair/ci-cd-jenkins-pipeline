pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                // Example for Python
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Unit and Integration Tests') {
            steps {
                echo 'Running Unit and Integration Tests...'
                // Example for pytest
                sh 'pytest tests/'
            }
        }

        stage('Code Analysis') {
            steps {
                echo 'Analyzing Code...'
                // Example for pylint
                sh 'pylint *.py'
            }
        }

        stage('Security Scan') {
            steps {
                echo 'Running Security Scan...'
                // Example for Bandit
                sh 'bandit -r .'
            }
        }

        stage('Deploy to Staging') {
            steps {
                echo 'Deploying to Staging...'
                // Placeholder for deployment steps
                sh 'echo "Deploy to staging server here"'
            }
        }

        stage('Integration Tests on Staging') {
            steps {
                echo 'Running Integration Tests on Staging...'
                // Placeholder for running tests on staging
                sh 'echo "Run tests against staging server"'
            }
        }

        stage('Deploy to Production') {
            steps {
                echo 'Deploying to Production...'
                // Placeholder for deployment steps
                sh 'echo "Deploy to production server here"'
            }
        }
    }

    post {
        always {
            echo 'Sending Notifications...'
            emailext (
                to: 'rnairadithi05@gmail.com',
                subject: "Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_STATUS})",
                body: """\
                Check console output at ${env.BUILD_URL} to view the results.
                """
            )
        }
    }
}
