#!/bin/sh
if grep -Fqe "Image is up to date" << EOF
`docker pull sudipta20449667/pythondocker:latest`
EOF
then
    echo "no update, just doing some cleaning"
    docker system prune --force
else
    echo "A newer version exits rerunning"
    docker stop cronspeed
    docker rm cronspeed
    docker run --privileged -d --name cronspeed --restart unless-stopped sudipta20449667/pythondocker:latest
fi
