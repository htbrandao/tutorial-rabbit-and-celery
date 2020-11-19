#!/bin/bash

echo "@ iniciando worker #1"
celery --app=tasks worker --queues=filarq30_1 \
    -n worker_1 \
    --loglevel=info \
    --pidfile=temp/worker_1.pid \
