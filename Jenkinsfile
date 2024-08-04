pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Docker Compose Build
                    sh 'docker-compose -f docker-compose.yml build --pull --no-cache'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Yeni versiyonu başlat ve eski versiyonu durdur
                    sh 'docker-compose -f docker-compose.yml up -d --remove-orphans'
                }
            }
        }
    }

    post {
        always {
            script {
                // Temizlik işlemleri 
                sh 'docker system prune -f'
            }
        }
    }
}
