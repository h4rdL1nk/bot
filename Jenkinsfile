#!/usr/bin/env groovy

@Library('standardLibraries') _

def awsAppEnv = ''
def awsEcrImg = ''

pipeline{
    agent {
        label 'workeraws'
    }
    stages{
        stage('Docker image build'){
            steps{
                script{
                    dockerBuildImage([
                        tag: "jenkins-${JOB_NAME}-${BUILD_NUMBER}-img",
                        options: "",
                        buildDir: "."
                    ])
                }
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
        stage('Deploy application to AWS'){
            steps{
                script{
                    def gitBranch = getGitValue([
                        param: "currentBranch",
                        dir: ""
                    ])
                    switch(gitBranch){
                        case 'master':
                            awsAppEnv = 'pro'
                            break
                        case ['testing','pre']:
                            awsAppEnv = 'pre'
                            break    
                        default: 
                            awsAppEnv = 'pre'
                            break     
                    }
                    awsEcsDeployApp([
                        awsRegion: "eu-west-1",
                        awsCredId: "aws-inftel-admin",
                        ecsClusterRegex: "^.*/CL.*-${awsAppEnv}\$",
                        ecsServiceRegex: "^.*/SVC-bot",
                        awsEcrImg: "${awsEcrImg}",
                        awsAppEnv: "${awsAppEnv}",
                        awsAppName: "bot",
                        deployTimeout: "120"
                    ])                
                }    
            }
        }
    }
    post {
        always {
            script {
                def commitMail = getGitValue([
                            param: "authorMail",
                            dir: ""
                    ])

                def commitHash = getGitValue([
                        param: "longHash",
                        dir: ""
                    ])

                def commitDate = getGitValue([
                        param: "commitDate",
                        dir: ""
                    ])

                def commitMsg = getGitValue([
                        param: "message",
                        dir: ""
                    ])

                echo "${commitHash} <${commitMail}> ${commitDate}"

                emailext(
                        from: "jenkins-ci@app.madisonmk.com",
                        to: "${commitMail}",
                        mimeType: 'text/html',
                        subject: "[${currentBuild.currentResult}] ${BUILD_DISPLAY_NAME} ${JOB_NAME}",
                        body: "<br>Finalizado ${JOB_NAME} ${BUILD_NUMBER}<br>Nodo:${NODE_NAME}<br>Commit: ${comitHash}<br>Fecha: ${commitDate}",
                        attachLog: true
                )
            }
        }
    }
}