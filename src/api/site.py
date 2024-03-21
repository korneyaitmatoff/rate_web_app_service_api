from loguru import logger
from requests import post, get, Response

from src.api.web_app_api import WebAppApi
from src.schemas.html_validation_schema import HtmlValidationDict


class SiteApi(WebAppApi):
    """Класс для работы с api методами модели site"""

    def __init__(self, path: str = 'site'):
        super().__init__(path=path)

    def get_site(self, site_id: int) -> Response:
        """Получение сайта по id"""

        url = f'{self.URL}:84/{self.path}/{site_id}'

        logger.debug(f"Отправка запроса: {url}")

        response = get(url=url)

        logger.debug(f"Получен ответ: {response.text}")

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

    def get_sites_by_category(self, category: str) -> Response:
        """Получение списка сайтов по категории

        Args:
            category: категория
        """
        logger.debug(f"Отправка запроса: {self.URL}:84/{self.path}/list/{category}")
        response = get(url=f'{self.URL}:84/{self.path}/list/{category}')
        logger.debug(f"Получен ответ: {response.text}")

        return response
