pipeline {
  agent any

  environment {
    DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
  }

  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/aam2k6/IMT2023558-calculator'
      }
    }

    stage('Install deps') {
      steps {
        sh 'python3 -m pip install --upgrade pip pytest || true'
        sh 'pip install pytest'
      }
    }

    stage('Run tests') {
      steps {
        sh 'pytest -q'
      }
    }

    stage('Build image') {
      steps {
        sh 'docker build -t ${DOCKERHUB_CREDENTIALS_USR}/calculator:latest .'
      }
    }

    stage('Login to Docker Hub') {
      steps {
        sh 'echo "${DOCKERHUB_CREDENTIALS_PSW}" | docker login -u "${DOCKERHUB_CREDENTIALS_USR}" --password-stdin'
      }
    }

    stage('Push image') {
      steps {
        sh 'docker push ${DOCKERHUB_CREDENTIALS_USR}/calculator:latest'
      }
    }
  }
}
