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
    def __init__(self, host='localhost', queue='Q'):
        self.host = host
        self.queue = queue


class RabbitMqServer(object):
    def __init__(self, server):
        self.server = server
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.server.host))
        self._channel = self._connection.channel()
        self._tem = self._channel.queue_declare(queue=self.server.queue)

    @staticmethod
    def callback(ch, method, properties, body):
        print("Received {}".format(body.decode("utf-8")))

    def start_server(self):
        self._channel.basic_consume(queue=self.server.queue,
                                    on_message_callback=self.callback,
                                    auto_ack=True)
        print('Waiting for messages: ')
        self._channel.start_consuming()


if __name__ == "__main__":
    server_config = RabbitMqConfig(host='localhost',
                                   queue='hello')
    server = RabbitMqServer(server_config)
    server.start_server()





