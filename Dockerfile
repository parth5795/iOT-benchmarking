# syntax=docker/dockerfile:1

FROM python:3.8.8
WORKDIR /usr/src/app
COPY . .
ENV LATCS7_PASSWORD MySambo12MySambo12
ENV DEVICE_ID 1
RUN pip3 install -r requirements.txt
CMD ["python3", "start.py"]
