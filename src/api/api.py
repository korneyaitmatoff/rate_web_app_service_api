from abc import ABC, abstractmethod


class Api(ABC):
    """Абстрактный класс для работы с api методами приложения"""
    URL: str