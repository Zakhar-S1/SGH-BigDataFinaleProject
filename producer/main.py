import argparse

import kafka
import produce_process
import reader

READER_MAP = {
    'csv': reader.CSVReader
}

PRODUCER_MAP = {
    'kafka': kafka.KafkaProducer
}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_path", help="Path to file for reader", type=str)
    parser.add_argument("--topic_name", help="Name of the topic for producer", type=str)
    parser.add_argument("--file_format", help="Format of the file (example: csv)", type=str)
    parser.add_argument("--type_of_producer", help="Type of the producer (example: kafka)", type=str)

    args = parser.parse_args()

    reader_class = READER_MAP[args.file_format]
    producer_class = PRODUCER_MAP[args.type_of_producer]
    produce_process = produce_process.ProduceProcess(
        reader=reader_class(file_path=args.file_path),
        producer=producer_class(topic=args.topic_name)
    )
    produce_process.run()
