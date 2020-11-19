#!/bin/bash

echo "# # iniciando celery"
celery --app=tasks worker --queues=filarq30_1 --loglevel=info
celery --app=tasks worker --queues=filarq30_2 --loglevel=info