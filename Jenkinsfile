pipeline {
  agent any

  stages {

      stage('Git Progress') {
        steps {
          git  branch: 'main', credentialsId: 'github_cred', url: 'https://github.com/Shin9184/devsecops-pipeline.git'
        }
      }

      stage ('Anchore Scan') {
        steps {
          script {
            def imageLine = 'tlqkddk123/flask-app'
            writeFile file: 'tlqkddk123/flask-app', text: imageLine
            anchore name: 'tlqkddk123/flask-app', engineCredentialsId: 'anchore_cred', bailOnFail: false
          }
        }
      }
  }
}
