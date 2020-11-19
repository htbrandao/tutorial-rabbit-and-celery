#!/bin/bash

echo "@ iniciando worker #2"
celery --app=tasks worker --queues=filarq30_2 \
    -n worker_2 \
    --loglevel=info \
    --pidfile=temp/worker_2.pid \
