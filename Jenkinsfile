#!/usr/bin/env groovy

pipeline{
    agent any

    stages{
        stage('Build'){
            steps{
                sh script: """
                    docker build -t test .
                """,returnStdout: true
            }
        }
    }
}