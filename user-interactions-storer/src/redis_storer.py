from redis import Redis


class RedisStorer:
    def __init__(self, redis_host, redis_port):
        self.__redis_server = Redis(host=redis_host, port=redis_port, decode_responses=True)

    @staticmethod
    def __increment_key_field(redis_server, key):
        if not redis_server.exists(key):
            redis_server.set(key, 0)
        redis_server.incr(key)

    @staticmethod
    def __decrement_key_field(redis_server, key):
        if not redis_server.exists(key):
            redis_server.set(key, 0)
        redis_server.decr(key)

    @staticmethod
    def __increment_hash_field(redis_server, hash_key, field):
        if not redis_server.hexists(hash_key, field):
            redis_server.hset(hash_key, field, 0)
        redis_server.hincrby(hash_key, field, 1)

    def handle_message(self, message):
        if 'source_version' not in message:
            print(message)
            return
        hash_key = f"{message['source_type']}:{message['source_version']}"
        inc_field_name = (f"{message['source_type']}:{message['source_version']}:"
                          f"{message['action']}:{message['target_type']}:{message['target_id']}")

        self.__increment_hash_field(self.__redis_server, hash_key, inc_field_name)
        self.__increment_hash_field(self.__redis_server, message['user_id'], f"{hash_key}:{inc_field_name}")

        if 'product_id' in message:
            match message['action']:
                case 'save_to_favorites':
                    self.__increment_key_field(self.__redis_server, f"product:{message['product_id']}:added")
                case 'remove_from_favorites':
                    self.__decrement_key_field(self.__redis_server, f"product:{message['product_id']}:added")
                case 'buy':
                    self.__increment_key_field(self.__redis_server, f"product:{message['product_id']}:bought")
                case 'share':
                    self.__increment_key_field(self.__redis_server, f"product:{message['product_id']}:shared")
