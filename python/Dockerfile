FROM python:3.6.5-alpine

COPY requirements.txt .

RUN pip install -r requirements.txt --upgrade

RUN mkdir /app
WORKDIR /app

COPY code/ /app

ENTRYPOINT ["python","/app/run.py"]
