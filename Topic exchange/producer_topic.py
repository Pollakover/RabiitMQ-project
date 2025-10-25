import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='51.250.26.59',
        port=5672,
        credentials=pika.PlainCredentials('guest', 'guest123')
    )
)
channel = connection.channel()

# Создание устойчивого обменника типа topic
channel.exchange_declare(exchange='IKBO-12-22_polyakov_topic',
                         exchange_type='topic', durable=True)

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World-'

channel.basic_publish(
    exchange='IKBO-12-22_polyakov_topic',
    routing_key=routing_key,
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    )
)
print(f'SENT: {message} with routing key {routing_key}')
connection.close()