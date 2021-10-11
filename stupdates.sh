#!/bin/sh
if grep -Fqe "Image is up to date" << EOF
`docker pull sudipta20449667/pythondocker:latest`
EOF
then
    echo "no update, just do cleaning"
    docker system prune --force
else
    echo "newest exist, rerunning"
    docker stop cronspeed
    docker rm cronspeed
    docker run --privileged -d --name cronspeed sudipta20449667/pythondocker:latest
fi
