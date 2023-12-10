from src.api.api import Api


class WebAppApi(Api):
    """Класс для работы с методами бизнесовой части приложений"""
    URL = 'http://127.0.0.1:8080'

    def __init__(self, path='/'):
        self.path = path
