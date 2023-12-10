from src.routes.router import Router
from src.services.html_validation_service import HtmlValidationService


class HtmlValidationRouter(Router):
    def __init__(self, service: HtmlValidationService, routes: list[dict], prefix: str = '/'):
        super().__init__(service=service, routes=routes, prefix=prefix)
