import pika
import os
from dotenv import load_dotenv

load_dotenv()
RABBITMQ_URL = os.getenv("RABBITMQ_LINK")

params = pika.URLParameters(RABBITMQ_URL)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('recieved in main')
    print(body)

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('started consuming...')

channel.start_consuming()

channel.close()
