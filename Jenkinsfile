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
                def customImage = docker.build("tlqkddk123/flask-app")
                customImage.push("${env.BUILD_ID}")
                customImage.push("latest")
              }
          }
        }
      }

      // stage ('Anchore Scan') {
      //   steps {
      //     script {
      //       def imageLine = 'tlqkddk123/flask-app'
      //       writeFile file: 'tlqkddk123/flask-app', text: imageLine
      //       anchore name: 'tlqkddk123/flask-app', engineCredentialsId: 'anchore_cred', bailOnFail: false
      //     }
      //   }
      // }
        
    stage('SSH Deploy') {
      steps {
        script {
          sshagent (credentials: ['instance_cred']) {
	      sh "ssh -o StrictHostKeyChecking=no ec2-user@192.168.4.179 docker run -d --name flask-app tlqkddk123/flask-app:${env.BUILD_ID}"
	      sh "ssh -o StrictHostKeyChecking=no ec2-user@192.168.4.179 sudo systemctl restart httpd"
          }
        }
      }
    }
  }
}

