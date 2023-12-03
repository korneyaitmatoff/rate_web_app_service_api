from datetime import datetime

from src.schemas.schema import Schema


class HtmlValidation(Schema):
    """Схема лога валидации html сайта"""
    id: int
    site_id: int
    logs: list[str]
    created_at: datetime
