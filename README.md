#Build and run container

docker build --no-cache -t bot .

docker run -it --entrypoint bash --rm -e SLACK_BOT_TOKEN=xoxb-247027687936-pbtMb
B5e1XqpDoIlYlqE8ijg bot