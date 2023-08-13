import redis


class InteractionsProcessor:
    def __init__(self, redis_host, redis_port):
        self.__redis_client = redis.Redis(host=redis_host, port=redis_port)

    def process_popular_product(self):
        products = {}
        for key in self.__redis_client.scan_iter('product:*:*'):
            product_id = key.decode('utf-8').split(':')[1]
            if product_id not in products:
                products[product_id] = 0
            products[product_id] += int(self.__redis_client.get(key))
        if not products:
            print("No products found")
            return
        
        print(f"All Products: {products}")
        print("-" * 50)
        print(f"Most popular: {max(products, key=products.get)}")
        print("#" * 50)
        print(" " * 50)
