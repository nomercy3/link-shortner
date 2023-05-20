from random import choice
from string import ascii_lowercase
from dataclasses import dataclass


@dataclass
class RandomizerService:
    @staticmethod
    def make_random_path() -> str:

        new_path = str()
        for i in range(10):
            new_path += choice(ascii_lowercase)

        print(len(new_path))
        return new_path
