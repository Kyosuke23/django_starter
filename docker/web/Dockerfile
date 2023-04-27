FROM python:3.10-slim

# コンソールのバッファを無効にする
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    cron \
    busybox-static \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/