from src.repositories.task_repository import TaskRepository
from src.schemas import Task, TaskDict
from src.services.service import Service


class TaskService(Service):
    repository: TaskRepository

    def __init__(self, repository: TaskRepository):
        super().__init__(repository=repository)

    def get_tasks(self) -> list[Task]:
        """Получение задачи по site_id"""
        return self.repository.get_tasks()

    def create_task(self, task: TaskDict) -> Task:
        """Создание задачи"""
        return self.repository.create_task(data=task)

    def delete_task(self, task_id: int):
        """Удаление задачи"""
        self.repository.delete_task(task_id=task_id)
