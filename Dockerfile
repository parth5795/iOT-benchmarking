# syntax=docker/dockerfile:1
FROM arm32v7/python:3.8.12-slim-buster
#FROM python:3.8.8
WORKDIR /usr/src/app
COPY . .
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get -y install gcc mono-mcs && \
    rm -rf /var/lib/apt/lists/*
RUN apt-get install libffi-dev && apt-get install libffi-devopenssl-dev && apt-get install python3-dev
RUN pip3 install -r requirements.txt
CMD ["python3", "start.py", "--sleep_time","30"]
