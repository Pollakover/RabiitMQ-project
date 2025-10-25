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

# Создание устойчивого обменника типа fanout
channel.exchange_declare(exchange='IKBO-12-22_polyakov_fanout',
                         exchange_type='fanout', durable=True)

message = ' '.join(sys.argv[1:]) or 'Hello World#'
channel.basic_publish(
        exchange='IKBO-12-22_polyakov_fanout',
    routing_key='',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    )
)
print(f'SENT: {message}')
connection.close()