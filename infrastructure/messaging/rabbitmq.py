import pika
import json

class RabbitMQClient:
    def __init__(self, queue_name):
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)

    def publish(self, message: dict):
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue_name,
            body=json.dumps(message)
        )
        print(f" [RABBITMQ] Enviado: {message}")
    
    def consume(self, callback):
        def wrapped_callback(ch, method, properties, body):
            data = json.loads(body)
            callback(data)
        
        self.channel.basic_consume(
            queue=self.queue_name,
            on_message_callback=wrapped_callback,
            auto_ack=True
        )
        print(f'[*] Esperando mensajes en la cola "{self.queue_name}".')
        self.channel.start_consuming()
