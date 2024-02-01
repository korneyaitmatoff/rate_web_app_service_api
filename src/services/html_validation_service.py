from json import dumps

from src.services.service import Service
from src.repositories.html_validation_repostory import HtmlValidationRepository
from src.schemas.html_validation_schema import (
    HtmlValidationDict as Hv_dict,
    HtmlValidation as Hv,
)
from src.handlers.html_validation_handler import HtmlValidationHandler as handler


class HtmlValidationService(Service):
    repository: HtmlValidationRepository

    def __init__(self, repository: HtmlValidationRepository):
        super().__init__(repository=repository)

    def get_log(self, site_id: int):
        """Получение лога"""
        return self.repository.get_log_by_site_id(site_id=site_id)

    def add_log(self, data: Hv_dict) -> Hv:
        """Добавление лога"""
        return self.create(data={
            'site_id': data['site_id'],
            'logs': dumps(handler().get_site_validation(data['site_id']))
        })

    def delete_log(self, log_id: int):
        """Удаление лога"""
        self.delete(filters=(self.repository.table.id == log_id,))
