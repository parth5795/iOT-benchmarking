# syntax=docker/dockerfile:1
FROM arm32v7/ubuntu:20.04
WORKDIR /usr/src/app
COPY . .
RUN apt-get update -y
RUN apt-get -y install wget
RUN wget http://ftp.us.debian.org/debian/pool/main/libs/libseccomp/libseccomp2_2.5.1-1_armhf.deb
RUN dpkg -i libseccomp2_2.5.1-1_armhf.deb
RUN apt-get -y install build-essential libssl-dev libffi-dev python3-pip python3-dev
RUN apt-get install -y ca-certificates
RUN apt-get clean
RUN pip3 install -r requirements.txt
CMD ["python3", "start.py"]
