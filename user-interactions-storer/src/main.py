import os

from kafka_consumer_wrapper import KafkaConsumerWrapper
from redis_storer import RedisStorer


def main():
    kafka_broker = os.environ['KAFKA_BROKER'] if 'KAFKA_BROKER' in os.environ else 'localhost:9092'
    redis_host = os.environ['REDIS_HOST'] if 'REDIS_HOST' in os.environ else 'localhost'
    redis_port = os.environ['REDIS_PORT'] if 'REDIS_PORT' in os.environ else 6379

    consumer = KafkaConsumerWrapper(kafka_broker, 'user-interaction')
    redis_storer = RedisStorer(redis_host, redis_port)

    while True:
        try:
            message = consumer.get_next_message()
        except Exception as e:
            print("Error consuming messages from Kafka", e)
            break

        try:
            redis_storer.handle_message(message.value)
        except Exception as e:
            print("Error storing message", e)
            break


if __name__ == '__main__':
    main()
