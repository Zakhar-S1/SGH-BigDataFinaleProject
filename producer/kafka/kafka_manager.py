from confluent_kafka import Producer, Consumer


class KafkaConnectionManager(object):
    _producer = None
    KAFKA_DELIVERY_TIMEOUT = 120000
    MESSAGE_MAX_BYTES = 1024 * 1024 * 20  # 20 mb

    def get_producer(self):
        # type: () -> Producer
        if not self._producer:
            self._producer = self._get_kafka_producer()
        return self._producer

    def _get_kafka_config(self):
        # type: () -> dict
        conf = {
            'bootstrap.servers': 'kafka:9092',
            'delivery.timeout.ms': self.KAFKA_DELIVERY_TIMEOUT,
            'security.protocol': 'PLAINTEXT',
            'compression.type': 'zstd',
            'sasl.mechanism': 'PLAIN',
            'message.max.bytes': self.MESSAGE_MAX_BYTES,
            'linger.ms': 20,
        }
        return conf

    def _get_kafka_producer(self):
        # type: () -> Producer
        conf = self._get_kafka_config()
        return Producer(conf)
