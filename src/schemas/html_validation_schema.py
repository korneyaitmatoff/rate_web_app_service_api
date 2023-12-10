from datetime import datetime
from typing_extensions import TypedDict

from src.schemas.schema import Schema


class HtmlValidation(Schema):
    """Схема лога валидации html сайта"""
    id: int
    site_id: int
    logs: str
    created_at: datetime


class HtmlValidationDict(TypedDict):
    """Схема dict лога валидации html сайта"""
    site_id: int
