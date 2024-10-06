pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'build'
        git branch: 'main', credentialsId: '448df686-fbb8-4108-bd3a-43231ea9ea06', url: 'https://github.com/farheen0204/test-project.git'
      }
    }


    stage('Complete') {
      steps {
        echo 'test complete'
        }
      }
    
  }
}
