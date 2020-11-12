#!/bin/bash

echo "# removendo container coelhomq"
docker container rm -f coelhomq &

echo "# removendo Flower"
pkill -9 flower &

echo "# removendo Celery"
pkill -9 celery &

echo "# removendo logs"
rm -v *.log

echo "# done"
