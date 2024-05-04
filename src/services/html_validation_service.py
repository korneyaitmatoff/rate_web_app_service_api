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
        site = SiteApi().get_site(site_id=site_id).json()
        sites_by_category = SiteApi().get_sites_by_category(category=site['category']).json()
        site_logs = self.get_log(site_id=site_id)

        errors_count: int = 0
        warnings_count: int = 0
        site_errors_counts: int = loads(site_logs[0].logs)['errors']['count']
        site_warnings_counts: int = loads(site_logs[0].logs)['warnings']['count']

        sites_logs = [self.get_log(site['id']) for site in sites_by_category]

        for log_el in sites_logs:
            for log in log_el:
                logs = loads(log.logs)

                errors_count += int(logs['errors']['count'])
                warnings_count += int(logs['warnings']['count'])

        errors_avg = round(errors_count / len(sites_logs))
        warnings_avg = round(warnings_count / len(sites_logs))
        errors_diff = errors_avg - site_errors_counts
        warnings_diff = warnings_avg - site_warnings_counts

        return {
            "errors": {
                "avg": errors_avg,
                "diff": round((100 * abs(errors_diff)) / errors_avg),
                "ml": 1 if errors_diff > 0 else 0,
                "stat": {log.created_at: loads(log.logs)['errors']['count'] for log in site_logs}
            },
            "warnings": {
                "avg": warnings_avg,
                "diff": round((100 * abs(warnings_diff)) / warnings_avg),
                "ml": 1 if warnings_diff > 0 else 0,
                "stat": {log.created_at: loads(log.logs)['warnings']['count'] for log in site_logs}
            }
        }
