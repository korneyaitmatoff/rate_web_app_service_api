from typing import Type

from sqlalchemy.orm import DeclarativeMeta

from src.repositories.repository import Repository
from src.schemas.css_validation_schema import CssValidationDict


class CssValidationRepository(Repository):
    """Репозиторй css-v логов"""

    def __init__(self, table: Type[DeclarativeMeta], database_handler):
        super().__init__(table=table, database_handler=database_handler)

    def add_log(self, data: CssValidationDict):
        """добавление лога в бд"""
        return self.create(data=data)

    def get_log(self, site_id: int):
        """Получение лога по id сайта"""
        return self.read(filters=(self.table.site_id == site_id,))
