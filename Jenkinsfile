pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Docker İmajını Oluştur
                    sh 'docker build -t notion_app_image .'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Mevcut konteyner varsa durdur ve sil
                    sh 'docker stop notion_app_container || true'
                    sh 'docker rm notion_app_container || true'

                    // Docker Konteynerini Başlat
                    sh 'docker run -d --name notion_app_container -p 6500:6500 notion_app_image'
                }
            }
        }
    }
}
