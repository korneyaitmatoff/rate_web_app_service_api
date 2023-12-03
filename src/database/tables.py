from datetime import datetime

from sqlalchemy import Column, VARCHAR, TIMESTAMP, Integer, TEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Tasks(Base):
    """Таблица задач для выполнения крон"""
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    site_id = Column(Integer, nullable=False)
    name = Column(VARCHAR, nullable=False)
    task = Column(VARCHAR, nullable=False)
    timeout = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)


class HtmlValidationLog(Base):
    """Таблица логов валидации html"""
    id = Column(Integer, primary_key=True, autoincrement=True)
    site_id = Column(Integer, nullable=False)
    logs = Column(TEXT, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)


class PerformanceLogs(Base):
    """Таблица логов нт"""
    id = Column(Integer, primary_key=True, autoincrement=True)
    site_id = Column(Integer, nullable=False)
