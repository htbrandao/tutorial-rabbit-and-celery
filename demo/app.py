#!/usr/bin/env python3

from time import sleep
from tasks import primeira_task, segunda_task


q1 = 'filarq30_1'
q2 = 'filarq30_2'

s = 'F4119597'

if __name__ == '__main__':
    while True:
        _1 = primeira_task.apply_async(queue=q1, args=[s])
        # _2 = segunda_task.apply_async(queues=q2, args=[s * 4])
        sleep(1)
