#Build and run container (local)

docker build --no-cache -t bot build

docker run -d --rm -e SLACK_BOT_TOKEN=xoxb-********************* -p8888:80 bot


#Jenkins CI

- Configure Jenkins task of type pipeline
    - Pipeline
        Definition: Pipeline script from SCM
            SCM: Git
                Repositories: https://github.
            Script Path: Jenkinsfile

- Launch task through SCM Polling or SCM Webhook