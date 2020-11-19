from time import sleep
from random import randint

from celery import Celery


rb_protocol = 'amqp'
rb_user = 'arq30'
rb_pass = 'arq30'
rb_host = 'localhost'
rb_port = '5672'
rb_broker = f'{rb_protocol}://{rb_user}:{rb_pass}@{rb_host}:{rb_port}/'

app = Celery('app', broker=rb_broker)


@app.task()
def primeira_task(s):
    s = s * randint(1, 5)
    sleep(randint(1, 5))
    return s


@app.task()
def segunda_task(s):
    s = f'FOI {len(s.split("F"))} VEZES'
    return s
