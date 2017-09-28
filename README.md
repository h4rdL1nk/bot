#Build and run container

docker build --no-cache -t bot .

docker run -d --rm --name but-run -e SLACK_BOT_TOKEN=xoxb-247027687936-GRcTackoGJO5Vz7bDzIBjAkg bot