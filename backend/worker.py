from celery import Celery

worker = Celery(
    "worker",
    broker="amqp://",
    backend="rpc://",
    include=["backend.tasks"]
)
