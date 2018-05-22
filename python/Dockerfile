FROM python:3.6.5-alpine

RUN pip install python-telegram-bot --upgrade

RUN mkdir /app
WORKDIR /app

COPY code/ /app

ENTRYPOINT ["python","/app/run.py"]
