from typing import List

from fastapi import FastAPI

from src.app import App
from src.database import tables

from src.repositories import HtmlValidationRepository
from src.repositories import TaskRepository

from src.services import HtmlValidationService
from src.services import TaskService

from src.schemas import HtmlValidation
from src.schemas import Task

from src.routes import HtmlValidationRouter
from src.routes import TaskRouter

server = (app := App(server=FastAPI())).get_app()

# Сервисы
html_service = HtmlValidationService(
    repository=HtmlValidationRepository(table=tables.HtmlValidationLog, database_handler=app.db_handler))
task_service = TaskService(
    repository=TaskRepository(table=tables.Tasks, database_handler=app.db_handler))

# Роутеры
app.register_routes([
    HtmlValidationRouter(
        service=html_service,
        routes=[
            {
                "path": "/{site_id}",
                "responses": {400: {"description": "Bad request"}},
                "response_model": HtmlValidation,
                "description": "Получение лога по site_id", "methods": ['GET'],
                "endpoint": html_service.get_log
            },
            {
                "path": "",
                "responses": {400: {"description": "Bad request"}},
                "response_model": HtmlValidation,
                "description": "Создание лога", "methods": ['POST'],
                "endpoint": html_service.add_log
            },
            {
                "path": "/{log_id}",
                "responses": {400: {"description": "Bad request"}},
                "description": "Удаление лога", "methods": ['DELETE'],
                "endpoint": html_service.delete_log
            },
        ],
        prefix='/html_val'
    ).get_router(),
    TaskRouter(
        service=task_service,
        routes=[
            {
                "path": "",
                "responses": {400: {"description": "Bad request"}},
                "response_model": list[Task],
                "description": "Получение списка задач", "methods": ['GET'],
                "endpoint": task_service.get_tasks
            },
            {
                "path": "",
                "responses": {400: {"description": "Bad request"}},
                "response_model": Task,
                "description": "Создание задачи", "methods": ['POST'],
                "endpoint": task_service.create_task
            },
            {
                "path": "/{task_id}",
                "responses": {400: {"description": "Bad request"}},
                "description": "Удаление задачи", "methods": ['DELETE'],
                "endpoint": task_service.delete_task
            },
        ],
        prefix='/task'
    ).get_router()
])
