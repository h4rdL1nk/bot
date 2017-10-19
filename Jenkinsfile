#!/usr/bin/env groovy

pipeline{
    agent any

    stages{
        stage('Build'){
            steps{
                sh script: """
                    ls -lrt
                """,returnStdout: true
            }
        }
    }
}