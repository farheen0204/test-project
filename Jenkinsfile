def fileContents
pipeline {
  agent any
  stages {
    stage('checkout code') {
      steps {
        echo 'checkout'
        git branch: 'main', credentialsId: '448df686-fbb8-4108-bd3a-43231ea9ea06', url: 'https://github.com/farheen0204/test-project.git'
      }
    }
    stage('readfile') {
      steps {
        script {
          fileContents = readFile 'Utilities/input.properties'          
        }
      }  
    }  
    stage('output') {
      steps {
        script {
          echo fileContents
        }
      }
    }

    // stage('Run') {
    //   steps {
    //     sh 'source /Users/arpitkhare/Selenium-Project/selenium_python_famework/.venv/bin/activate'
    //     sh 'pytest -v --html=reportgit.html'
    //   }
    // }

    stage('Complete') {
      steps {
        echo 'test complete'
      }
    }

  }
}
