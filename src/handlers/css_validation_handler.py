from xmltodict import parse
from json import dumps

from src.api.site import SiteApi
from src.api.css_validation import CssValidationApi


class CssValidationHandler:
    """Класс для работы с css-валидацией сайта"""
    SITE_NOT_FOUND_ERROR = "Сайт не был найден. Убедитесь в достоверности данных."

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

        return dumps({
            "errors": {
                "count": parse_result['env:Envelope']['env:Body']['m:cssvalidationresponse']['m:result']['m:errors'][
                    'm:errorcount'],
                "errors": parse_result['env:Envelope']['env:Body']['m:cssvalidationresponse']['m:result']['m:errors'][
                    'm:errorlist']
            },
            "warnings": {
                "count": parse_result['env:Envelope']['env:Body']['m:cssvalidationresponse']['m:result']['m:warnings'][
                    'm:warningcount'],
                "warnings":
                    parse_result['env:Envelope']['env:Body']['m:cssvalidationresponse']['m:result']['m:warnings'][
                        'm:warninglist']
            }
        })
