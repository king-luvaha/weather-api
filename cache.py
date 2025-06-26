import redis
import os
import json

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
r = redis.Redis.from_url(redis_url)

def cache_get(key):
    data = r.get(key)
    if data:
        return json.loads(data)
    return None

def cache_set(key, value, ex=43200):
    r.set(key, json.dumps(value), ex=ex)
