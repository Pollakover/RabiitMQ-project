import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='51.250.26.59',
        port=5672,
        credentials=pika.PlainCredentials('guest', 'guest123')
    )
)
channel = connection.channel()

# Создание устойчивой очереди
channel.queue_declare(queue='IKBO-12-22_polyakov_durable', durable=True)

channel.basic_publish(
    exchange='',
    routing_key='IKBO-12-22_polyakov_durable',
    body='Сообщение для устойчивой очереди',
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    )
)
print('SENT: Сообщение для устойчивой очереди')
connection.close()