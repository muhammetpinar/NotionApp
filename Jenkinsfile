pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Docker İmajını Oluştur
                    sh 'docker build -t NotionAppImage .'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Mevcut konteyner varsa durdur ve sil
                    sh 'docker stop NotionApp_container || true'
                    sh 'docker rm NotionApp_container || true'

                    // Docker Konteynerini Başlat
                    sh 'docker run -d --name NotionApp_container -p 6500:6500 NotionAppImage'
                }
            }
        }
    }
}
