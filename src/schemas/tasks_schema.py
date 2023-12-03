from src.schemas.schema import Schema


class Task(Schema):
    """Схема задачи"""

    id: int
    name: str
    site_id: int
    task: str
    timeout: int
