import requests


class CssValidationApi:
    """Класс для работы с валидацией css-кода"""

    @staticmethod
    def get_validation(site_url: str):
        response = requests.get(
            url=f"https://jigsaw.w3.org/css-validator/validator?uri={site_url}&warning2&profile=css2&output=soap12"
        )
    
        return response.text
