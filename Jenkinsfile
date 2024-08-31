pipeline {
    agent any

    environment {
        // Set MAVEN_HOME to the directory containing Maven
        MAVEN_HOME = 'C:\\Users\\rnair\\Downloads\\apache-maven-3.9.9-bin\\apache-maven-3.9.9'
        // Add Maven's bin directory to the PATH
        PATH = "${env.MAVEN_HOME}\\bin;${env.PATH}"
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                // Maven commands will now use the installation from the specified MAVEN_HOME
                bat 'mvn clean install'
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
                bat 'echo Security Scan not implemented for Windows'
            }
        }

        stage('Deploy to Staging') {
            steps {
                echo 'Deploying to staging...'
                bat 'echo Deploy to Staging not implemented for Windows'
            }
        }

        stage('Integration Tests on Staging') {
            steps {
                echo 'Running integration tests on staging...'
                bat 'echo Integration Tests not implemented for Windows'
            }
        }

        stage('Deploy to Production') {
            steps {
                echo 'Deploying to production...'
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
