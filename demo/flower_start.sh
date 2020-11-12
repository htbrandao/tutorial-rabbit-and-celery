#!/bin/bash

echo "# # flower para fila_guildarq30"
flower -A celery_tasks --port=5555
