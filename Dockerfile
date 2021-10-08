# syntax=docker/dockerfile:1
FROM arm32v7/python:3.8.12-slim-buster
#FROM python:3.8.8
WORKDIR /usr/src/app
COPY . .
RUN pip3 install -r requirements.txt
RUN apt-get install gcc
CMD ["python3", "start.py", "--sleep_time","30"]
