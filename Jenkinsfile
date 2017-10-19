#!/usr/bin/env groovy

@Library('standardLibraries') _

pipeline{
    agent any

    stages{
        stage('Docker image build'){
            steps{
                sh script: """
                    #!/bin/bash
                    set +x 
                    docker build -t jenkins-${JOB_NAME}-${BUILD_NUMBER}-img --no-cache .
                """
            }
        }
        stage('Docker image tests') {
            when{
                expression{
                    def gossCheck = sh script: "[ ! -e tests/goss/goss.yaml ]", returnStatus: true
                    return gossCheck
                }
            }
            steps{
                sh 'cd tests/goss && dgoss run jenkins-${JOB_NAME}-${BUILD_NUMBER}-img'
            }
        }
    }
}