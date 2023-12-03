from abc import ABC, abstractmethod

from fastapi import APIRouter

from src.services.service import Service


class RouterAbc(ABC):
    """Абстрактный класс маршрутизитора"""
    router: APIRouter
    service: Service

    @abstractmethod
    def register_routes(self, routes):
        """Регистрация роутов"""
        ...

    @abstractmethod
    def get_router(self):
        """Геттер роута"""
        ...
