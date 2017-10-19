#!/usr/bin/env groovy

pipeline{
    agent any

    stages{
        stage('Build'){
            steps{
                echo "Building image ..."
                sh script: """
                    #!/bin/bash

                    set +x 

                    docker build -t test .
                
                """
            }
        }
    }
}