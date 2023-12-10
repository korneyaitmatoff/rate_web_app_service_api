from w3c_validator import validate

from src.api.site import SiteApi


class HtmlValidationHandler:
    """Класс для работы с html-валидацией сайта"""
    SITE_NOT_FOUND_ERROR = "Сайт не был найден. Убедитесь в достоверности данных."

    @staticmethod
    def get_site_validation(site_id: int) -> list[str]:
        """Функция для html-валидации сайта

        Args:
            site_id: идентификатор сайта;
        """
        if not SiteApi(path='site').is_site_exists(site_id=site_id):
            return [HtmlValidationHandler.SITE_NOT_FOUND_ERROR]

        return [item['message'] for item in
                validate(SiteApi(path='site').get_site(site_id=site_id).json()['url'])['messages']]
