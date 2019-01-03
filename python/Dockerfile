FROM python:2-alpine3.7

RUN apk -U add docker --virtual build-deps musl-dev libffi-dev openssl-dev gcc

COPY requirements.txt .

RUN pip install -r requirements.txt --upgrade

RUN apk del build-deps

RUN mkdir /app
WORKDIR /app
COPY code/ /app

ENTRYPOINT ["python","/app/run.py"]
