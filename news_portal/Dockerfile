FROM alpine:latest

ENV PYTHONBUFFERED=1

RUN apk add --no-cache python3 py3-pip

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libc-dev make git libffi-dev openssl-dev libxml2-dev libxslt-dev

RUN pip3 install --no-cache --upgrade pip setuptools wheel

RUN apk add --no-cache bash

RUN mkdir -p /app

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000