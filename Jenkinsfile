#!/usr/bin/env groovy

pipeline{
    agent any

    stages{
        stage('Build'){
            steps{
                echo "Building image ..."
                sh script: """
                    #!/bin/bash

                    docker build -t test .
                
                """, returnStdout: true
            }
        }
    }
}