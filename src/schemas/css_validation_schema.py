from typing_extensions import TypedDict
from datetime import datetime


class CssValidationDict(TypedDict):
    """Схема dict лога валидации css сайта"""
    site_id: int


class CssValidationSchema(TypedDict):
    """Схема данных для записи в бд"""
    id: int
    site_id: int
    logs: str
    created_at: datetime
