import pika

RABBIT_ADDRESS=rabbit
QUEUE_NAME=plants
MESSAGE_BODY=input('Plant name: ')

# Rabbit connection
connection = pika.BlockingConnection(pika.ConnectionParameters(RABBIT_ADDRESS))
channel = connection.channel()

# Create a queue
channel.queue_declare(queue=QUEUE_NAME)

# Sends message
channel.basic_publish(exchange='',
                      routing_key=QUEUE_NAME,
                      body=MESSAGE_BODY)

print(" [x] Sent message")

connection.close()
