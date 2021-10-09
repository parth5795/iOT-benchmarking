# syntax=docker/dockerfile:1
FROM balenalib/raspberry-pi-python
WORKDIR /usr/src/app
COPY . .
RUN apt-get update -y
RUN apt-get -y install wget
RUN wget http://ftp.us.debian.org/debian/pool/main/libs/libseccomp/libseccomp2_2.5.1-1_armhf.deb
RUN dpkg -i libseccomp2_2.5.1-1_armhf.deb
RUN apt-get -y install build-essential libssl-dev libffi-dev python3-pip python3-dev
RUN apt-get update -y  --reinstall ca-certificates
RUN apt-get clean
ENV SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.cr
RUN pip3 install -r requirements.txt
CMD ["python3", "start.py"]
