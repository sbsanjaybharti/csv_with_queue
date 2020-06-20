import pika
import json

from ..config import Config as config


class RabbitMq():

    def __init__(self):
        """ Configure Rabbit Mq Server  """
        credentials = pika.PlainCredentials(config.RABBITMQ_USERNAME, config.RABBITMQ_PASSWORD)
        parameters = pika.ConnectionParameters(config.RABBITMQ_HOST, 5672, '/', credentials)
        self._connection = pika.BlockingConnection(parameters)
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue=config.RABBITMQ_QUEUE)

    def callback(self, ch, method, properties, body):

        # body = remove_trailing_commas(body.decode("utf-8"))
        # data = json.loads(body)
        # response = EventService.set(data['data'], data['source'])
        pass

    def publish(self, payload={}):
        """
        :param payload: JSON payload
        :return: None
        """
        print('========={}={}={}'.format(config.RABBITMQ_EXCHANGE, config.RABBITMQ_ROUTINGKEY, str(payload)))
        self._channel.basic_publish(exchange=config.RABBITMQ_EXCHANGE,
                                    routing_key=config.RABBITMQ_ROUTINGKEY,
                                    body=str(payload))

        print("Published Message: {}".format(payload))

    def close_connection(self):
        """
        :param payload: JSON payload
        :return: None
        """
        self._connection.close()

    def startserver(self):
        self._channel.basic_consume(
            queue=config.RABBITMQ_QUEUE,
            on_message_callback=self.callback,
            auto_ack=True)
        self._channel.start_consuming()