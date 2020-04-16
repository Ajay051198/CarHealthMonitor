import csv
import json
try:
    import pika
except Exception as e:
    print("Some modules are missing!", e)


class RabbitMqConfig(object):

    """
        This class configures the rabbit mq
    """
    def __init__(self, host='localhost', queue='Hello'):

        """
            This method is used to initialaise the server name and queue from where the data is received
        """
        self.host = host
        self.queue = queue
        # to clear the contents of a file or create the file if it doesn't already exist
        open('sensor1.txt', 'w').close()
        open('SensorData.CSV','w').close()
        open('TimeElaped.CSV','w').close()


class RabbitMqServer(object):
    """
        Initialise the server properties.
        - Local host tells that we are connected to a broker on local machine
          To connect to a broker on different machine we need to mention the
          IP Address or its name
        - Before sending we need to make sure the recipient queue exists.
          If we send a message to non-existing location, RabbitMQ will just drop
          the message.
    """
    def __init__(self, server):
        self.server = server
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.server.host))
        self._channel = self._connection.channel()
        self._tem = self._channel.queue_declare(queue=self.server.queue)
    message = {}

    @staticmethod
    def callback(ch, method, properties, body):
        """
            Whenever we receive a message, this callback function is called by the Pika library. 
            In our case this function will print on the screen the contents of the message.
        """
         
        message = body.decode("utf-8")
        print(f"Received {message}")
        # message = json.loads(str(message))
        message = message.replace('\'', '\"')
        data = json.loads(message)

        # iterating through the contents of a single packet sent from GUI and saving it in a file
        for i in range(len(data['sensor1Data'])):
            with open('SensorData.CSV', 'a+', newline='') as f:
                m = "{},{},{}\n".format(data['sensor1Data'][i], data['sensor2Data'][i], data['sensor3Data'][i])
                f.write(m)

        print(f"time: {data['time']}")
        with open('TimeElaped.CSV', 'a+', newline='') as f:
            f.write(str(data['time'])+'\n')

        with open('parameters.txt', 'w', newline='') as f:
            params = {"category1": data['category1'],
                      "category2": data['category2']}
            f.write(str(params))

    def start_server(self):
        """
            For that command to succeed we must be sure that a queue which we want to subscribe to exists. 
            Fortunately we're confident about that ‒ we've created a queue above ‒ using queue_declare.
        """
        self._channel.basic_consume(queue=self.server.queue,
                                    on_message_callback=self.callback,
                                    auto_ack=True)
        print('Waiting for messages: ')
        self._channel.start_consuming()


if __name__ == "__main__":
    server_config = RabbitMqConfig(host='localhost',
                                   queue='Hello')
    server = RabbitMqServer(server_config)
    server.start_server()