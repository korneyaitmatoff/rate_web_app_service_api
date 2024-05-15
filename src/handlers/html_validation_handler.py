from typing import Any

from w3c_validator import validate

from src.api.site import SiteApi


class HtmlValidationHandler:
    """Класс для работы с html-валидацией сайта"""
    SITE_NOT_FOUND_ERROR = "Сайт не был найден. Убедитесь в достоверности данных."

    @staticmethod
    def get_site_validation(site_id: int) -> dict[dict[str, int | list[dict[str, Any]]]] | str:
        """Функция для html-валидации сайта

        Args:
            site_id: идентификатор сайта;
        """
        if not SiteApi(path='site').is_site_exists(site_id=site_id):
            return HtmlValidationHandler.SITE_NOT_FOUND_ERROR

        result = {
            "errors": {
                "count": 0,
                "errors": []
            },
            "warnings": {
                "count": 0,
                "warnings": []
            }
        }

        for item in validate(SiteApi(path='site').get_site(site_id=site_id).json()['url'], verbose=True)['messages']:
            if item['type'] == "error":
                result['errors']['count'] += 1
                if len(item['message']) <= 256:
                    result['errors']['errors'].append(item)
            else:
                result['warnings']['count'] += 1
                if len(item['message']) <= 256:
                    result['warnings']['warnings'].append(item)

        return result
