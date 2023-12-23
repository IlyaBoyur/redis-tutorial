import redis


HOST = 'localhost'
PORT = 6379


def blocking_push(key: str):
    db = redis.Redis(host=HOST, port=PORT, decode_responses=True)
    [db.lpush(key, i) for i in range(10)]

def blocking_pop(key: str):
    db = redis.Redis(host=HOST, port=PORT, decode_responses=True)
    for _ in range(10):
        print(db.brpop(key))


if __name__ == "__main__":
    blocking_push("test")
    blocking_pop("test")
