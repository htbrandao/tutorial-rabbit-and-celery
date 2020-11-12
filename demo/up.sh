#!/bin/bash

echo "# Rabbit MQ"
./rabbit_start.sh &&

echo "# Celery"
./celery_workers.sh &&

echo "# Flower"
./flower_start.sh &&
