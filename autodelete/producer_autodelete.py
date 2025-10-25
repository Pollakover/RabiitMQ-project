import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='51.250.26.59',
        port=5672,
        credentials=pika.PlainCredentials('guest', 'guest123')
    )
)
channel = connection.channel()

# Создание автоудаляемой очереди
channel.queue_declare(queue='IKBO-12-22_polyakov_autodelete', auto_delete=True)

channel.basic_publish(
    exchange='',
    routing_key='IKBO-12-22_polyakov_autodelete',
    body='Сообщение для автоудаляемой очереди'
)
print('SENT: Сообщение для автоудаляемой очереди')
connection.close()