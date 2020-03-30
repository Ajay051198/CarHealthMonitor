try:
    import pika
except Exception as e:
    print("Some modules are missing!", e)

class MetaClass(type):
    
    _instance={}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


class RabbitMqConfig(metaclass = MetaClass):

    def __init__(self, queue='Q', host='localhost', exchange='', routing_key='Q'):
        self.queue = queue
        self.host = host
        self.exchange = exchange
        self.routing_key = routing_key


class RabbitMq():
    def __init__(self, server):
        self.server = server
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.server.host))
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue=self.server.queue)

    def publish(self, payload={}):
        self._channel.basic_publish(exchange=self.server.exchange, routing_key=self.server.routing_key, body=str(payload))
        print("Published Message:{}".format(payload))
        self._connection.close()


if __name__ == "__main__":
    server = RabbitMqConfig(queue='Q',
                            host='localhost',
                            exchange='',
                            routing_key='Q')
    rabbit_mq = RabbitMq(server)
    rabbit_mq.publish(payload={"Data": 22})


