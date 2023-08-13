import os
from time import sleep

from interactions_processor import InteractionsProcessor


def main():
    redis_host = os.environ['REDIS_HOST'] if 'REDIS_HOST' in os.environ else 'localhost'
    redis_port = os.environ['REDIS_PORT'] if 'REDIS_PORT' in os.environ else 6379

    while True:
        InteractionsProcessor(redis_host, redis_port).process_popular_product()
        sleep(1)


if __name__ == '__main__':
    main()
