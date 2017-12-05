pipeline {
    agent any
    options {
        timestamps()
        disableConcurrentBuilds()
    }
    stages {
        stage('Openshift login command'){
            steps{
                withCredentials([string(credentialsId: 'openshift-starter-token', variable: 'OS_TOKEN')]){
                    sh script: """
                        oc login https://api.starter-us-west-1.openshift.com --token=$OS_TOKEN
                    """
                }
            }
        }
    }
    post{
        always{
            deleteDir()
        }
    }
}