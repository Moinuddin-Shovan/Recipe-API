FROM python:3.7-alpine
MAINTAINER Moinuddin Kader

ENV PYTHONUNBUFFERED 1
# RECOMMENDED FOR DOCKER

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user