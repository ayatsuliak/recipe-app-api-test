"""
Django command to wait for database to be available
"""
import time  # noqa: F401
from psycopg2 import OperationalError as Psycopg2Error  # noqa: F401

from django.db.utils import OperationalError  # noqa: F401
from django.core.management.base import BaseCommand   # noqa: F401


class Command(BaseCommand):
    """Django command to wait for  database"""
    def handle(self, *args, **options):
        """Entry point for command"""
        self.stdout.write('Waiting for database...')
        db_up = False
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (OperationalError, Psycopg2Error):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
