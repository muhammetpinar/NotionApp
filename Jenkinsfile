pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Docker İmajını Oluştur
                    sh 'docker build -t my-app-image .'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Mevcut konteyner varsa durdur ve sil
                    sh 'docker stop my-app-container || true'
                    sh 'docker rm my-app-container || true'

                    // Docker Konteynerini Başlat
                    sh 'docker run -d --name my-app-container -p 6500:6500 my-app-image'
                }
            }
        }
    }
}
