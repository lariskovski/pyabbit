# pyabbit
RabbitMQ + Python project

## Basics

Check queues RabbitMQ has and how many messages are in them:

``sudo rabbitmqctl list_queues``

bin path: ``/opt/rabbitmq/sbin/rabbitmqctl``

## Setup

### RabbitMQ

``docker run -d --hostname rabbit --name rabbit -p 5672:5672 rabbitmq:3``

## Testing

Sending a message to the plants queue

``curl -X POST localhost:5000/api/plants -d '{"name":"rose", "primary_color": "red"}'``
