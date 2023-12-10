import requests
from allure import step, title


class TestHtmlValidationLog:
    URL = "http://127.0.0.1:8000"

    @title("Создание лога")
    def test_create_log(self):
        requests.post(
            url=f'{self.URL}/html_val',
            json={
                "site_id": 1,
                "logs": [
                    "data"
                ]
            }
        )
