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
        stage('Application acceptance tests') {
            when{
                expression{
                    def codeceptionCheck = sh script: "[ ! -d tests/codeception ]", returnStatus: true
                    return codeceptionCheck
                }
            }
            steps{
                sh script: """
                    #!/bin/bash
                    set +x
                    docker run -d -e ENV=dev --name jenkins-${JOB_NAME}-${BUILD_NUMBER}-run jenkins-${JOB_NAME}-${BUILD_NUMBER}-img
                    docker exec -i jenkins-${JOB_NAME}-${BUILD_NUMBER}-run composer require 'codeception/codeception:*'
                    docker exec -i jenkins-${JOB_NAME}-${BUILD_NUMBER}-run php vendor/bin/codecept run -c tests/codeception --no-colors --json
                    """
            }
        }
        stage('Push image to AWS') {
            steps{
                script{

                    def commitHash = getGitValue([
                        param: "longHash",
                        dir: ""
                    ])

                    awsEcrImg = dockerPushImageAws([
                        awsRegion: "eu-west-1",
                        awsCredId: "aws-inftel-admin",
                        localImageTag: "jenkins-${JOB_NAME}-${BUILD_NUMBER}-img",
                        pushImageTag: "bot:${commitHash}"
                    ])  

                }
            }
        }
    }
}