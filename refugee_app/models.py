from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = ['name']

class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.country} - {self.name}"

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

class Refugee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    id_serial = models.IntegerField()
    fin = models.CharField(max_length=10)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.father_name}"

    class Meta:
        index_together = [
            'first_name', 'last_name', 'father_name', 'birth_date', 'id_serial', 'fin'
        ]
