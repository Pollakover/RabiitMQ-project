import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='51.250.26.59',
        port=5672,
        credentials=pika.PlainCredentials('guest', 'guest123')
    )
)
channel = connection.channel()

# НЕ создаем очередь здесь, только отправляем
channel.basic_publish(
    exchange='',
    routing_key='IKBO-12-22_polyakov_exclusive',
    body='Сообщение для эксклюзивной очереди'
)
print('SENT: Сообщение для эксклюзивной очереди')
connection.close()