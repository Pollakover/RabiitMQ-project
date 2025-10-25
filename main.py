import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='51.250.26.59',
        port=5672,
        credentials=pika.PlainCredentials('guest', 'guest123')
    )
)
channel = connection.channel()

channel.queue_declare(queue='test_queue_2')

channel.basic_publish(
    exchange='',
    routing_key='test_queue_2',
    body='My first message'
)
print('SENT: My first message')
connection.close()
