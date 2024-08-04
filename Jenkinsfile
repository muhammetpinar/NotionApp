pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Docker image'ı oluştur
                    sh 'docker build -t my-flask-app .'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Docker Compose ile uygulamayı başlat
                    sh 'docker-compose -f docker-compose.yml up -d --remove-orphans'
                }
            }
        }
    }

    post {
        always {
            script {
                // Temizlik işlemleri (örneğin, kullanılmayan container'ları temizlemek)
                sh 'docker system prune -f'
            }
        }
    }
}
