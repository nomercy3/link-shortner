from typing import Any
from abc import ABC, abstractmethod


class StorageServiceInterface(ABC):

    @abstractmethod
    def save_data(self, data: str, key: str = None) -> Any:
        """
        Save data with/without key into storage
        :param data: data to store
        :param key: key for data to store in case of key-value storage
        :return: any data structure
        """
        pass

    @abstractmethod
    def get_data(self, key: str) -> Any:
        """
        Get data from storage by key or query
        :param key: key/query for data to return
        :return: any data structure
        """
        pass
