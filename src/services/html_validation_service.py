from json import dumps, loads

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

    def get_all_logs(self) -> list:
        return self.repository.get_logs()

    def get_log_stat(self, site_id):
        """Получение сайтовой статистики

        Args:
            site_id: идентификатор сайта
        """
        errors_count_list: dict[int, int] = {}

        for log in self.get_all_logs():
            if log.site_id not in errors_count_list:
                errors_count_list[log.site_id] = 0
            errors_count_list[log.site_id] += len(loads(log.logs))

        avg = sum(errors_count_list.values()) / float(len(errors_count_list))

        return {
            "avg": avg,
            "diff": avg - errors_count_list[int(site_id)],
            "stat": {log.created_at: len(loads(log.logs)) for log in self.get_log(site_id=site_id)}
        }
