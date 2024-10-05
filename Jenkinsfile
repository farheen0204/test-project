pipeline {
  agent any
  stages {
    stage('checkout code') {
      steps {
        git(url: 'https://github.com/farheen0204/test-project.git', branch: 'main')
      }
    }

    stage('log') {
      steps {
        sh 'source /Users/arpitkhare/Selenium-Project/selenium_python_famework/.venv/bin/activate'
        sh 'pytest -v --html=reportgit.html'
      }
    }

    stage('Complete') {
      steps {
        echo 'test complete'
      }
    }

  }
}
