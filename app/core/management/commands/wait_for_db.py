"""

Django command to wait for the database to become available
"""
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    """Django command to wait for db to become available"""

    def handle(self, *args, **options):
        pass
