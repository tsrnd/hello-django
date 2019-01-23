from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Seed data'

    def handle(self, *args, **options):
        self.stdout.write('Running all seeding scripts...')
        from myapp.seeds import users
        users.create_superuser()
