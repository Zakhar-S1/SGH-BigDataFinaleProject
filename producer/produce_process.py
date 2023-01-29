import json


class ProduceProcess:

    def __init__(self, reader, producer):
        self.reader = reader
        self.producer = producer

    def run(self):
        try:
            for data in self.reader.read():
                self.producer.produce(topic=self.producer.topic, message=json.dumps(data._asdict()))
            self.producer.flush()
        except Exception as ex:
            print(ex)
