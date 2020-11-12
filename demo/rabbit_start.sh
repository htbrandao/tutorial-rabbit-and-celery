#!/bin/bash

echo "# # removendo container anterior: coelhomq"
docker container rm -f coelhomq

echo "# # iniciando container: coelhomq"
docker run --hostname coelhomq --name coelhomq \
    -p 15672:15672 -p 5672:5672 \
    -e RABBITMQ_DEFAULT_USER=arq30 -e RABBITMQ_DEFAULT_PASS=arq30 \
    rabbitmq:3-management

echo "# # log coelhomq"
docker logs -f coelhomq
