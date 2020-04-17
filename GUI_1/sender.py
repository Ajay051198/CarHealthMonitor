try:
    import pika
except Exception as e:
    print("Some modules are missing!", e)


class RabbitMq(object):

    """
        This class is used to define the sender parameters of the AMQP protocol
    """

    def __init__(self, queue='Hello', host='localhost', exchange='', routing_key='Hello'):
        """
            This method is used to initialise the parameters required for AMQP

        Keyword Arguments:
            queue {str} -- [Before sending we need to make sure the recipient queue exists. 
                            If we send a message to non-existing location, RabbitMQ will just drop the message.] 
                            (default: {'Hello'})
            host {str} -- [Local host tells that we are connected to a broker on local machine
                            To connect to a broker on different machine we need to mention the IP Address or its name ] 
                            (default: {'localhost'})
            exchange {str} -- [the method by which data will be eexchanged] (default: {''})
            routing_key {str} -- [Every queue is assigned with a routing key inorder to differentiate the different queues. 
                                Queue name needs to be specified in the routing_key parameter] 
                                (default: {'Hello'})
        """

        self.queue = queue
        self.host = host
        self.exchange = exchange
        self.routing_key = routing_key

        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(self.host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(self.queue)

    def publish(self, payload):
        """
            This method is used to send the message to be received by the receiver
        """
        try:
            self.channel.basic_publish(
                exchange=self.exchange, routing_key=self.routing_key, body=(str(payload)))
        except:
            print("fucked again")
        print("Published ... ")


# if __name__ == "__main__":
#     rabbit_mq = RabbitMq(queue='Q',
#                             host='localhost',
#                             exchange='',
#                             routing_key='Q')
#     rabbit_mq.publish(payload={22})

    