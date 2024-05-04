from typing import Type

from sqlalchemy.orm import DeclarativeMeta

from src.schemas.html_validation_schema import HtmlValidationDict
from src.repositories.repository import Repository


class HtmlValidationRepository(Repository):
    """Репозиторий html-v логов"""

    def __init__(self, table: Type[DeclarativeMeta], database_handler):
        super().__init__(table=table, database_handler=database_handler)

    def create_html_v_log(self, data: HtmlValidationDict):
        """Создание лога"""
        self.create(data=data)

    def get_logs(self, filters: tuple = (), limit: int = 100):
        """Получени списка логов"""
        return self.read(filters=filters, limit=limit)

    def get_log_by_site_id(self, site_id):
        """Получение списка логов по id сайта"""
        return self.read(filters=(self.table.site_id == site_id,))

    def delete_log(self, id: int):
        """Удаление лога"""
        self.delete(filters=(self.table.id == id,))
