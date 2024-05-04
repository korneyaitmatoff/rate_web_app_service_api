from json import loads

from src.api.site import SiteApi
from src.services.service import Service
from src.schemas.css_validation_schema import CssValidationDict
from src.repositories.css_validation_repository import CssValidationRepository
from src.handlers.css_validation_handler import CssValidationHandler as handler


class CssValidationService(Service):
    repository: CssValidationRepository

    def add_log(self, data: CssValidationDict):
        return self.create(data={
            'site_id': data['site_id'],
            'logs': str(handler.get_site_validation(site_id=data['site_id']))
        })

    def get_log(self, site_id: int):
        return self.repository.get_log(site_id=site_id)

    def get_stat_log(self, site_id: int):
        site = SiteApi().get_site(site_id=site_id).json()
        sites_by_category = SiteApi().get_sites_by_category(category=site['category']).json()
        site_logs = self.get_log(site_id=site_id)

        errors_count: int = 0
        warnings_count: int = 0
        site_errors_counts: int
        site_warnings_counts: int

        sites_logs = [self.get_log(site['id']) for site in sites_by_category]

        for log_el in sites_logs:
            for log in log_el:
                logs = loads(log.logs)

                errors_count += int(logs['errors']['count'])
                warnings_count += int(logs['warnings']['count'])

                if log.site_id == site_id:
                    site_errors_counts = int(logs['errors']['count'])
                    site_warnings_counts = int(logs['warnings']['count'])

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
                "stat":  {log.created_at: loads(log.logs)['warnings']['count'] for log in site_logs}
            }
        }
