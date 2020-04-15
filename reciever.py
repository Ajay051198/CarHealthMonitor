import csv
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
        #to clear the contents of a file or create the file if it doesn't already exist
        open('sensor1.txt', 'w').close()
        open('SensorData.CSV','w').close()
        # open('TimeElapsed.CSV','w').close()



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

    @staticmethod
    def callback(ch, method, properties, body):
        """
            Whenever we receive a message, this callback function is called by the Pika library. 
            In our case this function will print on the screen the contents of the message.
        """
         
        message=body.decode("utf-8")
        print (f"Received {message}")

        #Read a file with existing data
        # a+ opens a file for appending and reading
        # it creates a file if it doesn't exist
        # with open('sensor1.txt', 'r') as fin:
        #     data = fin.read().splitlines(True)
        #     fin.close()
        
        listOfSensorData=[]
        # to convert message of type 'str' to 'list'
        listOfSensorReadings=list(message.split("], "))

        for i in range(len(listOfSensorReadings)):
            listOfSensorData.append(list(listOfSensorReadings[i].strip("[").strip("]").split(", ")))
        
        #storing data in a file 
        #if-else condition used to limit the number of readings stored
        file = open("SensorData.csv")
        row_count = sum(1 for row in file)

        # this might come handy if we want to restrict the data values
        if row_count > 100 : 
            #iterating through the contents of a single packet sent from GUI
            for i in range(len(listOfSensorData[1])):
                #storing data in a csv file
                with open('SensorData.CSV','a+', newline='') as f:
                    theWriter=csv.writer(f)
                    theWriter.writerow([listOfSensorData[0][i],listOfSensorData[1][i]])
            # print(f"time: {listOfSensorData[2][1]}")
            file = open("TimeElapsed.CSV","w")
            theWriter=csv.writer(file)
            theWriter.writerow([listOfSensorData[2][0],listOfSensorData[2][1]])
            file.close()
                
        else:
            for i in range(len(listOfSensorData[1])):
                #storing data in a csv file
                with open('SensorData.CSV','a+', newline='') as f:
                    theWriter=csv.writer(f)
                    theWriter.writerow([listOfSensorData[0][i],listOfSensorData[1][i]])
            f.close()
            #store time since previous service in a file
            print(f"time: {listOfSensorData[2][1]}")
            file = open("TimeElapsed.CSV","w")
            theWriter=csv.writer(file)
            theWriter.writerow([listOfSensorData[2][0],listOfSensorData[2][1]])
            file.close()

                


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