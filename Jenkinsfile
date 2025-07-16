pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning the GitHub repo...'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t automation-project .'
            }
        }

        stage('Run Tests in Docker') {
            steps {
                sh 'docker run --rm automation-project'
            }
        }
    }
}
