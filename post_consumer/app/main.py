import pika
import httpx
import json

credentials = pika.PlainCredentials('admin', 'admin')
props = {'connection_name': 'Pika Note consumer'}
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.0.212',
                                                               port=5672,
                                                               credentials=credentials,
                                                               client_properties=props
                                                               ))


def callback(ch, method, properties, body):
    receive_data = body.decode()
    result_json = json.loads(receive_data)

    ws_notification = f"http://192.168.0.212:8001/post/feed/posted"

    httpx.post(ws_notification, json={result_json})

    print(" [x] Received", receive_data, flush=True)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def consumer() -> None:
    channel = connection.channel()
    channel.queue_declare(queue='posts', durable=True)
    channel.basic_consume(queue='posts',
                          on_message_callback=callback,
                          auto_ack=False)
    channel.basic_qos(prefetch_count=1)

    print(' [*] Waiting for messages. To exit press CTRL+C', flush=True)
    channel.start_consuming()


consumer()
