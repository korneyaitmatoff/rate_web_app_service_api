from json import dumps, loads

from src.services.service import Service
from src.api.site import SiteApi
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

        site = SiteApi().get_site(site_id=site_id).json()
        sites_by_category = SiteApi().get_sites_by_category(category=site['category']).json()

        logs = [self.get_log(site['id']) for site in sites_by_category]

        for log_el in logs:
            for log in log_el:
                errors_count_list[log.site_id] = len(loads(log.logs))

        avg = round(sum(errors_count_list.values()) / float(len(errors_count_list)))
        diff = round(avg - errors_count_list[int(site_id)])

        return {
            "avg": avg,
            "diff": (100 * abs(diff)) / avg,
            "ml": 1 if diff > 0 else 0,
            "stat": {log.created_at: len(loads(log.logs)) for log in self.get_log(site_id=site_id)},
        }
