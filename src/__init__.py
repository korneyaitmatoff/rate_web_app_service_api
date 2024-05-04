from typing import List

from fastapi import FastAPI

from src.app import App
from src.database import tables

from src.repositories import HtmlValidationRepository
from src.repositories import CssValidationRepository
from src.repositories import TaskRepository

from src.services import HtmlValidationService
from src.services import CssValidationService
from src.services import TaskService

from src.schemas import HtmlValidation
from src.schemas import Task

from src.routes import CssValidationRouter
from src.routes import HtmlValidationRouter
from src.routes import TaskRouter

server = (app := App(server=FastAPI())).get_app()

# Сервисы
css_service = CssValidationService(
    repository=CssValidationRepository(table=tables.CssValidationLog, database_handler=app.db_handler))
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
            {
                "path": "/stat/{site_id}",
                "responses": {400: {"description": "Bad request"}},
                "description": "Получение статистики логов сайта", "methods": ['GET'],
                "endpoint": html_service.get_log_stat
            },
        ],
        prefix='/html_val'
    ).get_router(),
    CssValidationRouter(
        service=css_service,
        routes=[
            {
                "path": "/{site_id}",
                "responses": {400: {"description": "Bad request"}},
                "description": "Получение лога CSS", "methods": ['GET'],
                "endpoint": css_service.get_log
            },
            {
                "path": "",
                "responses": {400: {"description": "Bad request"}},
                "description": "Добавление лога CSS", "methods": ['POST'],
                "endpoint": css_service.add_log
            },
            {
                "path": "/stat/{site_id}",
                "responses": {400: {"description": "Bad request"}},
                "description": "Получние статистики лога CSS", "methods": ['GET'],
                "endpoint": css_service.get_stat_log
            }
        ],
        prefix='/css_val'
    ).get_router()
])
