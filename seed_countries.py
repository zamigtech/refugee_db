import sys, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task.settings')
import django
django.setup()

import json
from refugee_app.models import Country

with open("country-by-name.json") as f:
    countries = f.read()
    countries = countries.replace("'", '"')
    countries = json.loads(countries)
    for country in countries:
        Country.objects.create(name=country['country'])