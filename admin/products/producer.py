import pika
import os
from dotenv import load_dotenv

load_dotenv()
RABBITMQ_URL = os.getenv("RABBITMQ_LINK")

params = pika.URLParameters(RABBITMQ_URL)

connection = pika.BlockingConnection(params)

channel = connection.channel()

#def publish(method, body):
def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='Hello')


    
