from time import sleep
from random import random
from ..worker import worker


@worker.task
def add(x, y):
    sleep(random() * 2)
    if random() > 0.5:
        raise Exception("A problem occurred")
    return x + y


@worker.task
def minus(x, y):
    return x - y
