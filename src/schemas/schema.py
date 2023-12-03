from abc import ABC, abstractmethod

from src.repositories.repository import Repository


class Service(ABC):
    repository: Repository

    def __init__(self, repository: Repository):
        """Инит экземпляра класа

        Args:
            repository: репозиторий сущности
        """
        self.repository = repository

    def create(self, data: dict):
        """Саздание записи в бд"""
        return self.repository.create(data=data)

    def read(self, filters: tuple = (), limit: int = 100):
        """Чтение записи по id из бд"""
        return self.repository.read(filters=filters, limit=limit)

    def update(self, id: int, data: dict): ...

    def delete(self, filters: tuple):
        return self.repository.delete(filters=filters)
