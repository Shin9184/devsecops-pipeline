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
            def imageLine = 'python:3'
            writeFile file: 'python:3', text: imageLine
            anchore name: 'python:3', engineCredentialsId: 'anchore_cred', bailOnFail: false
          }
        }
      }
  }
}
