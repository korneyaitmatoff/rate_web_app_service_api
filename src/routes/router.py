from fastapi import APIRouter

from src.services.service import Service
from src.routes.router_abc import RouterAbc


class Router(RouterAbc):
    """Родительский метод маршрутизатора"""

    def __init__(self, service: Service, routes: list[dict], prefix: str = "/"):
        self.service = service
        self.router = APIRouter(prefix=prefix)

        self.register_routes(routes=routes)

    def register_routes(self, routes):
        for route in routes:
            self.router.add_api_route(**route)

    def get_router(self):
        return self.router
