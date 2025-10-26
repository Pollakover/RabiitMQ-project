import pika
import sys
import time


def callback(ch, method, properties, body):
    message = body.decode()
    routing_key = method.routing_key
    print(f"RECEIVED: {message} with routing key {routing_key}")

    # Подсчет символов - для определения времени сна
    sleep_time = message.count('-')
    if sleep_time > 0:
        print(f"Sleeping for {sleep_time} seconds...")
        time.sleep(sleep_time)

    print("INFO: Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='51.250.26.59',
        port=5672,
        credentials=pika.PlainCredentials('guest', 'guest123')
    )
)
channel = connection.channel()

channel.exchange_declare(exchange='IKBO-12-22_polyakov_topic',
                         exchange_type='topic', durable=True)

# Создание временной очереди
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

binding_keys = ["*.error", "*.warning"]

for binding_key in binding_keys:
    channel.queue_bind(
        exchange='IKBO-12-22_polyakov_topic',
        queue=queue_name,
        routing_key=binding_key
    )
    print(f"Binding queue to routing key: {binding_key}")

channel.basic_qos(prefetch_count=1)
channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback
)

print('Waiting for messages...')
channel.start_consuming()