def fileContents
pipeline {
  agent any
  stages {
    stage('checkout code') {
      steps {
        git(url: 'https://github.com/farheen0204/test-project.git', branch: 'main')
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
