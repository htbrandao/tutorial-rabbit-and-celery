#!/bin/bash

echo "# # iniciando celery em fila_guildarq30"
celery --app=celery_tasks worker --queues=fila_guildarq30 --loglevel=info
