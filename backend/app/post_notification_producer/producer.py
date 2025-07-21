import pika
import json
from app.config import settings


def producer(user_id: int, friends: list) -> bool:
    print("user id:", user_id, "friends", friends)
    credentials = pika.PlainCredentials(settings.RABBITMQ_USER, settings.RABBITMQ_PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=settings.RABBITMQ_HOST,
                                                                   port=settings.RABBITMQ_PORT,
                                                                   credentials=credentials
                                                                   ))

    channel = connection.channel()
    channel.queue_declare(queue=settings.RABBITMQ_QUEUE, durable=True)
    channel.basic_publish(exchange='',
                          routing_key=settings.RABBITMQ_ROUTER_KEY,
                          body=json.dumps({"id": user_id,
                                           "friends": friends
                                           }),
                          properties=pika.BasicProperties(
                                delivery_mode=1,
                            ))
    connection.close()
    return True
