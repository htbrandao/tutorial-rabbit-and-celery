from time import sleep
from random import randint

from celery import Celery


rb_protocol = 'amqp'
rb_user = 'arq30'
rb_pass = 'arq30'
rb_host = 'localhost'
rb_port = '5672'
rb_broker = f'{rb_protocol}://{rb_user}:{rb_pass}@{rb_host}:{rb_port}/'

app = Celery('app', broker=rb_broker, backend='amqp')

q1 = 'filarq30_1'
q2 = 'filarq30_2'


@app.task
def primeira_task(s):
    print('1 >>')
    sleep(randint(2, 5))
    s = s * randint(1, 5)
    return s


@app.task
def segunda_task(s):
    print('2 <<')
    s = f'INFO e ACAO {len(s.split())} VEZES'
    return s
