from abc import ABC, abstractmethod
from typing import Type

from sqlalchemy.orm import DeclarativeMeta

from src.database.handler import DatabaseHandler


class Repository(ABC):
    """Абстрактный класс для работы репозиториями"""
    db_engine: DatabaseHandler
    table: Type[DeclarativeMeta]

    def __init__(self, table: Type[DeclarativeMeta], database_handler):
        """Инит экземпляра класса

        Args:
            table: таблица сущности
        """
        self.db_engine = database_handler
        self.table = table

    def create(self, data: dict):
        """Создание объекта

        data: данные для создания записи
        """
        return self.db_engine.insert(table=self.table, data=data)

    def read(self, filters: tuple = (), limit: int = 100):
        """Чтение из таблицы

        Args:
            filters: фильтр для выборки данных
            limit: ограничение по кол-ву записей
        """
        return self.db_engine.select(table=self.table, filters=filters, limit=limit)

    def update(self, id: int, data: dict):
        """Изменение объекта

        Args:
            id: id объекта
            data: новые данные объекта
        """

        self.db_engine.update(table=self.table, filters=(self.table.id == id,), data=data)

    def delete(self, filters: tuple):
        """Удаление данных

        Args:
            filters: фильтр для выборки данных
        """
        self.db_engine.delete(table=self.table, filters=filters)
