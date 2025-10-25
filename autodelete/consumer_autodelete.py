import pika

def callback(ch, method, properties, body):
    print(f"RECEIVED: {body.decode()}")

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='51.250.26.59',
        port=5672,
        credentials=pika.PlainCredentials('guest', 'guest123')
    )
)
channel = connection.channel()

channel.queue_declare(queue='IKBO-12-22_polyakov_autodelete', auto_delete=True)

channel.basic_consume(
    queue='IKBO-12-22_polyakov_autodelete',
    on_message_callback=callback,
    auto_ack=True
)

print('Waiting for messages...')
channel.start_consuming()