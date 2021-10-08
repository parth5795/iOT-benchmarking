# syntax=docker/dockerfile:1
FROM arm32v7/ubuntu:20.04
#FROM python:3.8.8
WORKDIR /usr/src/app
COPY . .
sudo apt -y install python3-pip
RUN pip3 install -r requirements.txt
CMD ["python3", "start.py", "--sleep_time","30"]
