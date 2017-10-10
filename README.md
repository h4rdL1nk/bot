#Build and run container

docker build --no-cache -t bot build

docker run -d --rm -e SLACK_BOT_TOKEN=xoxb-********************* -p8888:80 bot
