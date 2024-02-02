from requests import post, get, Response
from loguru import logger

from src.api.web_app_api import WebAppApi
from src.schemas.html_validation_schema import HtmlValidationDict


class SiteApi(WebAppApi):
    """Класс для работы с api методами модели site"""

    def __init__(self, path: str = '/'):
        super().__init__(path=path)

    def get_site(self, site_id: int) -> Response:
        """Получение сайта по id"""

        response = get(url=f'{self.URL}/{self.path}/{site_id}')

        logger.debug(f"Получен запрос: {response.text}")

        return response

    def create_site(self, data: HtmlValidationDict) -> Response:
        """Создание сайта"""
        return post(url=f'{self.URL}/{self.path}', json=data)

    def is_site_exists(self, site_id: int) -> bool:
        """Метод для проверки существования сайта в сервисе бизнеса

        Args:
            site_id: идентификатор сайта;
        """
        return bool(self.get_site(site_id=site_id).json())
