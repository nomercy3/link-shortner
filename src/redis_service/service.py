from dotenv import load_dotenv
from os import getenv
from typing import Dict

from src.redis_service.storage_service_int import StorageServiceInterface
import redis


class RedisService(StorageServiceInterface):
    def __init__(self):
        load_dotenv()
        _host = getenv('REDIS_HOST')
        _port = getenv('REDIS_PORT')

        self.redis_service = redis.Redis(
            host=_host,
            port=_port,
            db=0
        )

    def save_data(self, data: str, key: str = None) -> Dict:
        if not isinstance(data, str) or not isinstance(key, str):
            raise TypeError

        try:
            self.redis_service.set(name=key, value=data)
            return {key: data}
        except redis.exceptions.ConnectionError:
            raise ConnectionError

    def get_data(self, key: str) -> Dict:
        if not isinstance(key, str):
            raise TypeError

        try:
            value = self.redis_service.get(key)
            if value:
                return {key: value.decode()}
            else:
                raise ValueError
        except redis.exceptions.ConnectionError:
            raise ConnectionError
