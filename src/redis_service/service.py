from dotenv import load_dotenv
from os import getenv
from typing import Dict

import redis


class RedisService(object):
    def __init__(self):
        load_dotenv()

        _host_ = getenv('REDIS_HOST')
        _port_ = getenv('REDIS_PORT')

        self.redis_server = redis.Redis(
            host=_host_,
            port=int(_port_),
            db=0  # db number
        )

    def set_key_value(self, key: str, value: str) -> Dict:
        if not isinstance(value, str) or not isinstance(key, str):
            raise TypeError

        try:
            self.redis_server.set(key, value)
            return {key: value}
        except (redis.exceptions.ConnectionError, IOError):
            return {}

    def get_value_for_key(self, key: str) -> Dict:
        if not isinstance(key, str):
            raise TypeError

        try:
            value = self.redis_server.get(key)
            return {key: value.decode()}
        except (redis.exceptions.ConnectionError, IOError, AttributeError):
            return {}
