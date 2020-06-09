from flask import Flask, jsonify, request
import pika

# RabbitMQ config
RABBIT_ADDRESS=localhost
QUEUE_NAME=plants
MESSAGE_BODY=''

# Rabbit connection
connection = pika.BlockingConnection(pika.ConnectionParameters(RABBIT_ADDRESS))
channel = connection.channel()

# Create a queue
channel.queue_declare(queue=QUEUE_NAME)

# API
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/health')
    def health():
        return jsonify({'Ailve': True})

    @app.route('/api/plants', methods=['POST'])
    def create_plant():
        body = request.get_json()
        if body is None:
            return(jsonify({message: abort 422}))
        else:
            new_name = body.get('name', None)
            new_primary_color = body.get('primary_color', None)

        try:
            MESSAGE_BODY=jsonify({
            'success': True,
            'plant': new_name,
            'primary_color': new_primary_color
            })
            # Sends message
            channel.basic_publish(exchange='',
                      routing_key=QUEUE_NAME,
                      body=MESSAGE_BODY)
            connection.close()

        except Exception as e:
            print(e)

    return app

create_app().run()
