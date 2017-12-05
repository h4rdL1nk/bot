pipeline {
    agent any
    options {
        timestamps()
        disableConcurrentBuilds()
    }
    stages {
        stage('Openshift login command'){
            steps{
                withCredentials([usernamePassword(credentialsId: 'openshift-starter-token', variable: 'OS_TOKEN')]) {

                }
                sh script: """
                    echo $OS_TOKEN
                """
            }
        }
    }
    post{
        success{
            deleteDir()
        }
    }
}