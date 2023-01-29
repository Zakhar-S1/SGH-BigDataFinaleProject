from typing import AnyStr

from confluent_kafka import Producer, Message, KafkaError

from .kafka_manager import KafkaConnectionManager


class NotDeliveredToKafkaException(Exception):
    pass


def log_messages(err, msg):
    # type: (KafkaError, Message) -> None
    if err:
        log_message = '{} | {}'.format(msg.value(), err.str())
        print(log_message)
        raise NotDeliveredToKafkaException(err.name())


class KafkaProducer(object):

    def __init__(self, topic):
        # type: (...) -> None
        self.topic = topic
        self.connection_manager = KafkaConnectionManager()

    def get_producer(self):
        # type: () -> Producer
        return self.connection_manager.get_producer()

    def produce(self, topic, message):
        # type: (AnyStr, AnyStr) -> None
        producer = self.get_producer()

        producer.produce(topic, message, on_delivery=log_messages)

    def flush(self):
        # type: () -> None
        self.get_producer().flush()
