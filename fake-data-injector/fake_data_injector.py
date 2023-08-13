import json
import os

from faker import Faker
from kafka import KafkaProducer

source_types_actions = {
    'web_app': ('click', 'hover'),
    'ios_app': 'tap',
    'android_app': 'tap',
}

source_type_versions = {
    'web_app': ['1.0.0', '1.0.1', '1.0.2'],
    'ios_app': ['1.0.0', '1.0.1', '1.0.2'],
    'android_app': ['1.0.0', '1.0.1', '1.0.2'],
}

target_type_ids = {
    'button': ['login', 'register', 'save_to_favorites', 'remove_from_favorites', 'buy', 'share'],
    'link': ['home', 'about', 'user-info'],
    'image': ['logo', 'banner'],
    'video': ['tutorial', 'demo'],
}

product_actions = ['save', 'buy', 'share']

product_ids = [
    'shampoo',
    'computer',
    'fridge',
    'tv',
    'phone',
]

user_ids = [
    'a1b2c3d4e5f6',
    'b1c2d3e4f5g6',
    'c1d2e3f4g5h6',
    'd1e2f3g4h5i6',
    'e1f2g3h4i5j6',
]


def generate_user_interaction(fake: Faker) -> dict:
    source_type = fake.random_element(elements=(source_types_actions.keys()))
    target_type = fake.random_element(elements=target_type_ids.keys())
    target_id = fake.random_element(elements=target_type_ids[target_type])
    action = fake.random_element(elements=source_types_actions[source_type])
    if target_id == 'login' or target_id == 'register':
        user_id = 'anonymous'
    else:
        user_id = fake.random_element(elements=user_ids)

    fake_data = {
        'user_interaction_id': fake.uuid4(),
        'user_id': user_id,
        'source_type': source_type,
        'source_version': fake.random_element(elements=source_type_versions[source_type]),
        'action': action,
        'target_type': target_type,
        'target_id': target_id,
        'timestamp': fake.unix_time(),
    }

    if action in product_actions:
        fake_data['product_id'] = fake.random_element(elements=product_ids)

    return fake_data


def main():
    kafka_broker = os.environ['KAFKA_BROKER'] if 'KAFKA_BROKER' in os.environ else 'localhost:9092'
    producer = KafkaProducer(
        bootstrap_servers=[kafka_broker],
        value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    if not producer.bootstrap_connected():
        print("Producer not connected to Kafka broker")
        return

    fake = Faker()
    for i in range(100):
        user_interaction = generate_user_interaction(fake)
        producer.send(topic='user-interaction', value=user_interaction)
        print("Sent message", i)


if __name__ == '__main__':
    main()
