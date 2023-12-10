from typing import Type

from sqlalchemy.orm import DeclarativeMeta

from src.schemas import TaskDict
from src.repositories.repository import Repository


class TaskRepository(Repository):
    """Репозиторй html-v логов"""

    def __init__(self, table: Type[DeclarativeMeta], database_handler):
        super().__init__(table=table, database_handler=database_handler)

    def get_tasks(self):
        """Получение списка задач"""
        return self.read(filters=())

    def create_task(self, data: TaskDict):
        """Создание задачи"""
        return self.create(data=data)

    def delete_task(self, task_id: int):
        """Удаление задачи"""
        self.delete(filters=(self.table.id == task_id,))
