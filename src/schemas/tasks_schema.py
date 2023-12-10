from typing_extensions import TypedDict

from src.schemas.schema import Schema


class Task(Schema):
    """Схема задачи"""

    id: int
    name: str
    site_id: int
    task: str
    timeout: int


class TaskDict(TypedDict):
    """Схема словаря задачи"""
    name: str
    site_id: int
    task: str
    timeout: int
