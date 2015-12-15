FROM ubuntu:latest
MAINTAINER Hive Solutions

EXPOSE 8080

ENV LEVEL INFO
ENV SERVER netius
ENV SERVER_ENCODING gzip
ENV HOST 0.0.0.0
ENV PORT 8080
ENV MONGOHQ_URL mongodb://localhost:27017
ENV PUSHER_APP_ID PUSHER_APP_ID
ENV PUSHER_KEY PUSHER_KEY
ENV PUSHER_SECRET PUSHER_SECRET
ENV GITHUB_ID GITHUB_ID
ENV GITHUB_SECRET GITHUB_SECRET
ENV GITHUB_REDIRECT_URL GITHUB_REDIRECT_URL
ENV PYTHONPATH /src

ADD requirements.txt /
ADD extra.txt /
ADD src /src

RUN apt-get update && apt-get install -y -q python python-setuptools python-dev python-pip
RUN pip install -r /requirements.txt && pip install -r /extra.txt && pip install --upgrade netius

CMD python /src/metrium/main.py
