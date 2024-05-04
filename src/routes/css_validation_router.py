from src.routes.router import Router
from src.services.css_validation_service import CssValidationService


class CssValidationRouter(Router):
    def __init__(self, service: CssValidationService, routes: list[dict], prefix: str = '/'):
        super().__init__(service=service, routes=routes, prefix=prefix)
