# pyabbit
RabbitMQ + Python project

## Basics

Check queues RabbitMQ has and how many messages are in them:

``sudo rabbitmqctl list_queues``

## Setup

### RabbitMQ

``docker run -d --hostname rabbit --name rabbit -p 5672:5672 rabbitmq:3``
