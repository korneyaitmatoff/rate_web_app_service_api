from xmltodict import parse
from json import dumps

from src.api.site import SiteApi
from src.api.css_validation import CssValidationApi


class CssValidationHandler:
    """Класс для работы с css-валидацией сайта"""
    SITE_NOT_FOUND_ERROR = "Сайт не был найден. Убедитесь в достоверности данных."

    @staticmethod
    def parse_errors(errors, key) -> list:
        result = []

        for data in errors:
            if isinstance(data[key], list):
                for el in data[key]:
                    if 'java.lang.Exception' not in el['m:message']:
                        if len(el['m:message']) <= 100:
                            result.append(el['m:message'])
            else:
                if 'java.lang.Exception' not in data[key]['m:message']:
                    if len(data[key]['m:message']) <= 100:
                        result.append(data[key]['m:message'])

        return result

    @staticmethod
    def get_site_validation(site_id: int) -> str:
        """Функция для html-валидации сайтаjr

        Args:
            site_id: идентификатор сайта;
        """
        if not SiteApi(path='site').is_site_exists(site_id=site_id):
            return CssValidationHandler.SITE_NOT_FOUND_ERROR

        parse_result = parse(
            xml_input=CssValidationApi.get_validation(
                site_url=SiteApi(path='site').get_site(site_id=site_id).json()['url']
            )
        )

        try:
            return dumps({
                "errors": {
                    "count":
                        parse_result['env:Envelope']['env:Body']['m:cssvalidationresponse']['m:result']['m:errors'][
                            'm:errorcount'],
                    "errors": CssValidationHandler.parse_errors(
                        errors=parse_result['env:Envelope']['env:Body']['m:cssvalidationresponse']['m:result']
                        ['m:errors']['m:errorlist'],
                        key='m:error'
                    )
                },
                "warnings": {
                    "count":
                        parse_result['env:Envelope']['env:Body']['m:cssvalidationresponse']['m:result']['m:warnings'][
                            'm:warningcount'],
                    "warnings":
                        CssValidationHandler.parse_errors(
                            errors=parse_result['env:Envelope']['env:Body']['m:cssvalidationresponse']['m:result']
                            ['m:warnings']['m:warninglist'],
                            key='m:warning'
                        )
                }
            })
        except KeyError:
            return dumps({
                "errors": {
                    "count": 0,
                    "errors": [
                        "Не удалось считать данные сайта. "
                        "Проверьте, что доступ к сайту не ограничивают сторонние утилиты."
                    ]
                },
                "warnings": {
                    "count": 0,
                    "warnings": [
                        "Не удалось считать данные сайта. "
                        "Проверьте, что доступ к сайту не ограничивают сторонние утилиты."
                    ]
                }
            })
