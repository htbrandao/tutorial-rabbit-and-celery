#!/usr/bin/env python3

from loguru import logger
from celery import Celery

from time import sleep
from random import randint
from datetime import datetime

logger.add("tasks.log", rotation="1 MB")

rb_protocol = 'amqp'
rb_user = 'arq30'
rb_pass = 'arq30'
rb_host = 'localhost'
rb_port = '5672'
rb_broker = f'{rb_protocol}://{rb_user}:{rb_pass}@{rb_host}:{rb_port}/'
rb_queue = 'fila_guildarq30'

logger.info(f'Conectando em {rb_broker}')

celery = Celery('celery_tasks', broker=rb_broker)


@celery.task()
def primeira_task(n: int, ts: str):
    s = f'sao {ts} e eu escrevo: {n}'
    logger.info('>> primeira_task')
    logger.info(s)
    return s

@celery.task()
def segunda_task(n: int, ts: str):
    s = f'sao {ts} e eu escrevo: {n}'
    logger.info('>> primeira_task')
    logger.info(s)
    return s


if __name__ == '__main__':
    
    while True:
        ts = datetime.now().strftime("%H:%M:%S-%m/%d/%Y")
        n = randint(1, 100)
        primeira_task.apply_async(queue=rb_queue, args=[ts, n])
        segunda_task.apply_async(queue=rb_queue, args=[ts, n])
        sleep(2)
