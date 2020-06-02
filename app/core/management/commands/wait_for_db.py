import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    """django command to pause execution until database is available"""
    def handle(self,*args,**options):
        """handle the command"""
        self.stdout.write('waiting for database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable waiting for 1 second....')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
