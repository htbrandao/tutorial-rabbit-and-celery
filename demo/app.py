#!/usr/bin/env python3

from time import sleep
from datetime import datetime
from tasks import primeira_task, segunda_task


q1 = 'filarq30_1'
q2 = 'filarq30_2'

s = 'INFORMACAO '

if __name__ == '__main__':
    while True:
        try:
            print(f'*** {datetime.now()}')
            _1 = primeira_task.apply_async(args=[s], queue=q1)
            _1 = _1.get()
            _2 = segunda_task.apply_async(args=[_1], queue=q2)
            sleep(3)
        except KeyboardInterrupt:
            break
