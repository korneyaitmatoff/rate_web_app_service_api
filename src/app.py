from fastapi import FastAPI
from fastapi import APIRouter

from src.database.handler import DatabaseHandler


class App:
    """Класс для управления сервером"""
    db_handler: DatabaseHandler
    server: FastAPI

    def __init__(self, server: FastAPI):
        self.server = server
        self.db_handler = DatabaseHandler()

        self.test_db_connection()

    def register_routes(self, routes: list[APIRouter]):
        """Метод для регистрации роутов"""
        for router in routes:
            self.server.include_router(router)

    def test_db_connection(self):
        """Регистрация и проверка соединения"""
        self.db_handler.test_connection()

    def get_app(self):
        """Получить объект приложени"""
        return self.server
