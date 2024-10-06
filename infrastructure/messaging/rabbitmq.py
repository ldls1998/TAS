import pika

class RabbitMQ:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='asignaciones')

    def publicar_evento(self, mensaje):
        self.channel.basic_publish(exchange='', routing_key='asignaciones', body=mensaje)
        print(f" [x] Enviado: {mensaje}")

    def cerrar_conexion(self):
        self.connection.close()