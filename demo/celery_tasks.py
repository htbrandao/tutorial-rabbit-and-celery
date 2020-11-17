#!/usr/bin/env python3

from loguru import logger
from celery import Celery

from time import sleep
from random import randint
from datetime import datetime

rb_protocol = 'amqp'
rb_user = 'arq30'
rb_pass = 'arq30'
rb_host = 'localhost'
rb_port = '5672'
rb_broker = f'{rb_protocol}://{rb_user}:{rb_pass}@{rb_host}:{rb_port}/'
rb_queue = 'fila_guildarq30'

celery = Celery('celery_tasks', broker=rb_broker)


@celery.task(acks_late=True)
def processamento_lento(n: int, ts: str):
    # TODO: processamento que demora muito
    s = f'ts:{ts} n: {n}'
    logger.info('>> processamento_lento')
    logger.info(s)
    return s

@celery.task(acks_late=True)
def segunda_task(n: int, ts: str):
    # TODO: pegar saida do processamento lento
    s = f'ts:{ts} n: {n}'
    logger.info('>> segunda_task')
    logger.info(s)
    return s


if __name__ == '__main__':
    logger.info(f'Conectando em {rb_broker}')
    
    while True:
    
        ts = datetime.now().strftime("%H:%M:%S-%m/%d/%Y")
        n = randint(1, 100)
        lento = processamento_lento.apply_async(queue=rb_queue, args=[n, ts])
        logger.info(ts, n)
    
        ts = datetime.now().strftime("%H:%M:%S-%m/%d/%Y")
        res = lento.get()
        segunda = segunda_task.apply_async(queue=rb_queue, args=[res, ts])
        logger.info(ts, n)
        
        sleep(2)
