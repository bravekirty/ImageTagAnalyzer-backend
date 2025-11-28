import redis
import json
from app.config import settings


config = {
    "host": settings.REDIS_HOST,
    "port": settings.REDIS_PORT,
    "decode_responses": True,
}

if settings.REDIS_PASSWORD:
    config["password"] = settings.REDIS_PASSWORD


redis_client = redis.Redis(**config)


def get_cached_data(key):
    data = redis_client.get(key)
    return json.loads(data) if data else None


def set_cached_data(key, data, expire=3600):
    redis_client.setex(key, expire, json.dumps(data))
