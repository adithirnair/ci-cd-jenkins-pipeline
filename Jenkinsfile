pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                bat 'mvn clean install'  // Use 'bat' instead of 'sh' for Windows
            }
        }

        stage('Unit and Integration Tests') {
            steps {
                echo 'Running unit and integration tests...'
                bat 'mvn test'
            }
        }

        stage('Code Analysis') {
            steps {
                echo 'Running code analysis...'
                bat 'mvn sonar:sonar'
            }
        }

        stage('Security Scan') {
            steps {
                echo 'Running security scan...'
                // Replace the Linux-specific commands with Windows equivalents, if necessary
                bat 'echo Security Scan not implemented for Windows'
            }
        }

        stage('Deploy to Staging') {
            steps {
                echo 'Deploying to staging...'
                // Add your deployment commands here
                bat 'echo Deploy to Staging not implemented for Windows'
            }
        }

        stage('Integration Tests on Staging') {
            steps {
                echo 'Running integration tests on staging...'
                // Add your test commands here
                bat 'echo Integration Tests not implemented for Windows'
            }
        }

        stage('Deploy to Production') {
            steps {
                echo 'Deploying to production...'
                // Add your deployment commands here
                bat 'echo Deploy to Production not implemented for Windows'
            }
        }
    }

    post {
        always {
            echo 'Sending Notifications...'
            emailext (
                to: 'rnairadithi05@gmail.com',
                subject: "Jenkins Pipeline - Build #${env.BUILD_NUMBER} - ${currentBuild.result}",
                body: "Build #${env.BUILD_NUMBER} completed with status: ${currentBuild.result}"
            )
        }
    }
}

