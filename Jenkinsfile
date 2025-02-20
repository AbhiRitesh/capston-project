pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'capstonproject'
    }

    stages {
        stage('Build') {
            steps {
                script {
                    // Build the Docker image
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run unit tests inside a Docker container
                    docker.image("${DOCKER_IMAGE}").inside {
                        sh 'pytest'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Run the Docker container
                    sh "docker run -d -p 5000:5000 ${DOCKER_IMAGE}"
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}