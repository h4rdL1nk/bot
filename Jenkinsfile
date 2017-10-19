#!/usr/bin/env groovy

pipeline{
    agent any

    stages{
        stage('Build'){
            steps{
                script{
                    sh script: """
                        docker build -t test .
                    """, returnStdout: true
                }
            }
        }
    }
}