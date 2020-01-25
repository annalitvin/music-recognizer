FROM ubuntu:16.04

FROM python:3.7-alpine

COPY ./requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
