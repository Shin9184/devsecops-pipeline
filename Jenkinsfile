pipeline {
  agent any

  stages {

      stage('Git Progress') {
        steps {
          git  branch: 'main', credentialsId: 'github_cred', url: 'https://github.com/Shin9184/devsecops-pipeline.git'
        }
      }
      
      stage('Slack Notification') {
        steps {
          slackSend (channel: 'pipeline', color: '#FFFF00', message: "STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
        }
      }

      stage('Push Image') {
        steps {
          script {
            checkout scm
              docker.withRegistry('https://registry.hub.docker.com', 'dockerhub_cred') {
                def customImage = docker.build("shin9184/flask")
                customImage.push("${env.BUILD_ID}")
                customImage.push("latest")
              }
          }
        }
      }

      stage ('Anchore Scan') {
        steps {
          script {
            def imageLine = 'tlqkddk123/flask'
            writeFile file: 'tlqkddk123/flask', text: imageLine
            anchore name: 'tlqkddk123/flask', engineCredentialsId: 'anchore_cred', bailOnFail: false
          }
        }
      }
        
    stage('SSH Deploy') {
      steps {
        script {
          sshagent (credentials: ['instance_cred']) {
            sh "ssh -o StrictHostKeyChecking=no ec2-user@192.168.4.179 docker rm -f flask"
            sh "ssh -o StrictHostKeyChecking=no ec2-user@192.168.4.179 docker run -d --net flask-nginx --name flask shin9184/flask:${env.BUILD_ID}"
          }
        }
      }
    }
  }
}
