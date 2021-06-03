from django.db import models
import datetime
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, null = True, on_delete = models.PROTECT)

    def __str__(self):
        return self.name


class Director(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, null = True,  on_delete = models.PROTECT)

    def __str__(self):
        return f"{self.first_name} {self.last_name}" 


class Film(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField(default=datetime.date.today)
    created_in_country = models.ForeignKey(Country, on_delete=models.PROTECT)
    available_in_countries = models.ManyToManyField(Country, related_name = 'available_in_countries', blank = True)
    category = models.ManyToManyField(Category, related_name = 'films', blank = True)
    director = models.ManyToManyField(Director, related_name = 'films', blank =True)
    url = models.URLField(null = True, blank = True)
    poster = models.ImageField(upload_to='posters/', null = True, blank = True) # will go to the media folder

    def __str__(self):
        return self.title
