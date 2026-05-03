"""Basic connection example.
"""

import redis
from redis_lru import RedisLRU

r = redis.Redis(
    host='redis-16578.crce198.eu-central-1-3.ec2.cloud.redislabs.com',
    port=16578,
    decode_responses=True,
    username="default",
    password="nujG2yqWQL4eQtiheeJNkmkMWewnbRgb",
)

success = r.set('foo', 'bar')
# True

result = r.get('foo')
print(result)
# >>> bar

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def f(x):
    print(f"Function call f({x})")
    return x


if __name__ == '__main__':
    print(f"Result f(3): {f(3)}")
    print(f"Result f(3): {f(3)}")