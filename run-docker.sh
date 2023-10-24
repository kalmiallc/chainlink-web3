#!/bin/bash
if [ "$1" = "install" ]; then
    docker build -t chainlink-web3 .
else
    docker run -t --name chainlink-web3-container chainlink-web3 ./run-script.sh $1

    if [ "$1" = "build" ]; then
        rm -rf dist
        docker cp chainlink-web3-container:/docker-app/dist ./dist
    fi

    docker rm -f chainlink-web3-container
fi