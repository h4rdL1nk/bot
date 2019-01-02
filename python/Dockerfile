FROM python:2-alpine3.7

RUN apk -U add --virtual build-deps musl-dev libffi-dev openssl-dev gcc

COPY requirements.txt .

RUN pip install -r requirements.txt --upgrade

RUN apk del build-deps

RUN mkdir /app
WORKDIR /app
COPY code/ /app

RUN mkdir -p /app/video/example
COPY sample.mp4 /app/video/example/sample.mp4

ENTRYPOINT ["python","/app/run.py"]
