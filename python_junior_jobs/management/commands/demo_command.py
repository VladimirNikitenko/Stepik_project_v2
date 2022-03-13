from django.core.management import BaseCommand
from python_junior_jobs.models import Company, Specialty, Vacancy


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('test')