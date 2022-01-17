import jenkins.model.*

jenkins = Jenkins.instance
pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                withCredentials(
                    usernamePassword(
                        credentialsId :jenkins - user - github ,
                        passwordVariable: "${GIT_PASSWORD}", usernameVariable: "${GIT_USERNAME}")) {
                    // Get some code from a GitHub repository
                    sh("""
              git config --global credential.username ${GIT_USERNAME}
              git config --global credential.helper "!echo password=${GIT_PASSWORD}; echo"
              git clone https://github.com/varnitsingh/calculator
              echo "pulled the code"
              """)
                        }
            }
        }
        stage('test') {
            steps {
                sh('python3 test.py')
            }
        }
    }
}
