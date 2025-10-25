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

# Создание обменника типа direct
channel.exchange_declare(exchange='IKBO-12-22_polyakov_direct',
                         exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World*'

channel.basic_publish(
    exchange='IKBO-12-22_polyakov_direct',
    routing_key=severity,
    body=message
)
print(f'SENT: {message} with routing key {severity}')
connection.close()