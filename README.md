#Build and run container

docker build --no-cache -t bot build

docker run -d --rm -e SLACK_BOT_TOKEN=xoxb-247027687936-5N3gIH5N0YEeBcvhGMKqoyIu -p8888:80 bot