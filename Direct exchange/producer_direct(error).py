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

channel.exchange_declare(exchange='IKBO-12-22_polyakov_direct',
                         exchange_type='direct')

severity = "error"
message = "Критическая ошибка!*"

channel.basic_publish(
    exchange='IKBO-12-22_polyakov_direct',
    routing_key=severity,
    body=message
)
print(f'SENT: {message} with routing key {severity}')
connection.close()