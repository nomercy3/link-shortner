from src.redis_service.service import RedisService
from src.randomizer.service import RandomizerService

from dataclasses import dataclass
from dotenv import load_dotenv
from os import getenv


@dataclass
class ShortnerService:
    load_dotenv()

    redis_service = RedisService()
    randomizer_service = RandomizerService()

    def shorten(self, full_link: str) -> str:
        if not isinstance(full_link, str):
            raise TypeError

        domain = getenv('DOMAIN')

        new_path = self.randomizer_service.make_random_path()
        short_link = f'https://{domain}/{new_path}'

        try:
            self.redis_service.save_data(
                key=short_link,
                data=full_link
            )
            return short_link
        except ConnectionError:
            raise

    def full_link(self, short_link: str) -> str:
        if not isinstance(short_link, str):
            raise TypeError

        try:
            full_link_dict = self.redis_service.get_data(key=short_link)
            return full_link_dict.get(short_link)
        except ValueError:
            raise
        except ConnectionError:
            raise
