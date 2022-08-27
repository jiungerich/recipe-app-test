"""

Django command to wait for the database to become available
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    """Django command to wait for db to become available"""

    def handle(self, *args, **options):
        """Entrypoint for command"""

        db_up = False
        self.stdout.write('Waiting for database...')

        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
