import pika

RABBIT_ADDRESS=rabbit
QUEUE_NAME=plants

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RABBIT_ADDRESS))

channel = connection.channel()

channel.queue_declare(queue=QUEUE_NAME)


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")


channel.basic_consume(
    queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
