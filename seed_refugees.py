import sys, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task.settings')
import django
django.setup()
import random

from refugee_app.models import City, Country, Refugee

from django_seed import Seed

seeder = Seed.seeder()
seeder.add_entity(Refugee, 2000, {
    'first_name': lambda x: seeder.faker.first_name(),
    'last_name': lambda x: seeder.faker.last_name(),
    'father_name': lambda x: seeder.faker.first_name(),
    'birth_date': lambda x: seeder.faker.date_of_birth(),
    'id_serial': lambda x: random.randint(10000000, 99999999),
    'fin': lambda x: random.randint(1000000, 9999999),
    'city': City.objects.all().order_by('?').first()
})

seeder.execute()