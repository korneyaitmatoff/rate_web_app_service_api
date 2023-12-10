from src.routes.router import Router
from src.services import TaskService


class TaskRouter(Router):
    def __init__(self, service: TaskService, routes: list[dict], prefix: str = '/'):
        super().__init__(service=service, routes=routes, prefix=prefix)
