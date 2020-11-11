#!/usr/bin/env python3

from loguru import logger
from celery import Celery

from time import sleep
from random import randint
from datetime import datetime

logger.add("log.log", rotation="1 MB")

rb_protocol = 'amqp'
rb_user = 'arq30'
rb_pass = 'arq30'
rb_host = 'coelhomq'
rb_port = '5672'
rb_broker = f'{rb_protocol}://{rb_user}:{rb_pass}@{rb_host}:{rb_port}'


celery = Celery('fila_guildarq30', broker=rb_broker, backend=rb_protocol)


@celery.task()
def primeira_task(n):
    logger.info('>> primeira_task')
    logger.info(f'eu deveria escrever: {n}')
    sleep(2)

@celery.task()
def segunda_task(ts):
    logger.info('>> primeira_task')
    logger.info(f'eu deveria escrever: {ts}')
    sleep(2)


if __name__ == '__main__':
    numero = randint(1, 100)
    timestamp = datetime.now().strftime("%H:%M:%S-%m/%d/%Y")
    primeira_task(numero)
    segunda_task(timestamp)
