from time import sleep
from ..worker import worker


@worker.task
def add(x, y):
    sleep(2)
    return x + y


@worker.task
def minus(x, y):
    return x - y
