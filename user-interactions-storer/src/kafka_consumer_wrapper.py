import json

from kafka import KafkaConsumer


class KafkaConsumerWrapper:
    def __init__(self, kafka_broker, topic):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=[kafka_broker],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='user-interactions-storer',
            value_deserializer=lambda x: json.loads(x.decode('utf-8')))

    def get_next_message(self):
        return next(self.consumer)
