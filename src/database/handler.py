from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)


class DatabaseHandler:
    """Класс для работы с базой данных"""

    def __init__(self):
        self.url = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        self.engine = create_engine(url=self.url)
        self.session = None

    def __enter__(self):
        """Контекстный менеджер, создание сессии"""

        self.create_session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Контекстный менеджер, закрытие сессии"""

        if exc_type:
            raise Exception(
                f'Произошла ошибка во время работы с БД!\n'
                f'\tТип:      {exc_type}\n'
                f'\tЗначение: {exc_val}\n'
                f'\tСтек:     {exc_tb}'
            )

        self.close_session()

    def create_session(self):
        """Создание сессии"""

        self.session = sessionmaker(bind=self.engine)()

    def close_session(self):
        """Закрытие сессии"""

        self.session.close()

    def test_connection(self):
        """Проверка соединения с бд"""

        self.create_session()
        self.session.execute(text("SELECT 1;"))
        self.close_session()

    def select(self, table, filters: tuple = (), limit: int = 1000) -> list:
        """Получение данных из таблицы"""

        return self.session.query(table).filter(*filters).limit(limit).all() if tuple else self.session.query(
            table).limit(limit).all()

    def insert(self, table, data: dict):
        """Добавление записи"""

        self.session.add(record := table(**data))
        self.session.commit()
        self.session.refresh(record)

        return record

    def delete(self, table, filters: tuple):
        """Удаление записи"""

        self.session.query(table).filter(*filters).delete()
        self.session.commit()

    def update(self, table, filters: tuple, data: dict):
        self.session.query(table).filter(*filters).update(data)
        self.session.commit()
