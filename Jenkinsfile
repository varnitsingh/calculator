pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                    sh('''
              git clone https://github.com/varnitsingh/calculator
              echo "pulled the code"
              ''')
            }
        }
        stage('test') {
            agent {
                docker { image 'python' }
            }
            steps {
                sh('python3 test.py')
            }
        }
    }
}
