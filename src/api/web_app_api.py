from src.api.api import Api
from config import API_HOST, API_PORT


class WebAppApi(Api):
    """Класс для работы с методами бизнесовой части приложений"""
    URL = f'{API_HOST}'

    def __init__(self, path='/'):
        self.path = path
