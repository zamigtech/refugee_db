import sys, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task.settings')
import django
django.setup()

from refugee_app.models import City, Country

from django_seed import Seed

seeder = Seed.seeder()
seeder.add_entity(City, 70, {
    'name': lambda x: seeder.faker.city(),
    'country': lambda x: Country.objects.get(id=15)
})

seeder.execute()