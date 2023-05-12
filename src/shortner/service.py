from src.redis_service.service import RedisService

from dataclasses import dataclass
from dotenv import load_dotenv
from os import getenv
from random import randint, choice
from string import ascii_lowercase
from typing import Dict

def test_shorten():
    service = ShortnerService()
    # mock data
    result = service.make_short()
    # check result
    # check mocks
    

# Теперь нужно сделать из этого апишку
@dataclass
class ShortnerService:
    load_dotenv()

    redis_service = RedisService()

    # make_short -> shorten
    # Замокать данные (домен, путь??) 
        # Нужно сделать MockStorageService  
    # Проверить поведение (ссылка сохранена)
    def make_short(self) -> str:
        domain = getenv('DOMAIN') # прокинуть мок в тестах
        input_link = self._prompt_user_input_('Place your full link: ')

        new_path = self._make_random_path_(str(input_link))
        short_link = f'https://{domain}/{new_path}'

        self._save_link_(
            full_link=input_link,
            short_link=short_link
        )

        print(short_link)
        return short_link

    # get_full_link -> full_link
    def get_full_link(self) -> str:
        input_short_link = self._prompt_user_input_('Place your short link: ')

        full_link_dict = self._get_link_(input_short_link)
        print(full_link_dict.get(input_short_link))
        return full_link_dict.get(input_short_link)

    def _save_link_(self, full_link: str, short_link: str) -> Dict:
        saved_object = self.redis_service.set_key_value(
            key=short_link,
            value=full_link
        )
        return saved_object

    # метод небольшой, используется в одном месте, нет смысла выносить.
    def _get_link_(self, short_link: str) -> Dict:
        saved_object = self.redis_service.get_value_for_key(
            key=short_link
        )
        return saved_object

    @staticmethod
    def _prompt_user_input_(prompt):
        return input(prompt)

    @staticmethod
    def _make_random_path_(link: str) -> str:

        new_path = str()
        for i in range(len(link)):
            if i >= 10:
                break
            elif i % 2 == 0:
                new_path += choice(ascii_lowercase)
            else:
                new_path += str(randint(0, 9))

        return new_path
