#!/usr/bin/env groovy

pipeline{
    agent any

    stages{
        stage('Build'){
            steps{
                script{
                    echo "Building image ..."
                    sh script: """
                        docker build -t test .
                    """, returnStdout: true
                }
            }
        }
    }
}