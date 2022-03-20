pipeline {
  agent any

  stages {

      stage('Git Progress') {
        steps {
          git  branch: 'main', credentialsId: 'github_cred', url: 'https://github.com/Shin9184/devsecops-pipeline.git'
        }
      }

      stage('Push Image') {
        steps {
          script {
            checkout scm
            docker.withRegistry('https://registry.hub.docker.com', 'dockerhub_cred') {
              def customImage = docker.build("shin/flask")
              customImage.push("${env.BUILD_ID}")
              customImage.push("latest")
            }
          }
        }
      }

      stage ('Anchore Scan') {
        steps {
          script {
            def imageLine = 'shin/flask'
            writeFile file: 'shin/flask', text: imageLine
            anchore name: 'shin/flask', engineCredentialsId: 'anchore_cred', bailOnFail: false
          }
        }
      }
        
    stage('SSH Deploy') {
      steps {
        script {
          sshagent (credentials: ['instance_cred']) {
            sh "ssh -o StrictHostKeyChecking=no ec2-user@192.168.4.179 docker run -p 8080 -d --name flask-app shin9184/flask:${env.BUILD_ID}"
          }
        }
      }
    }
  }
}
