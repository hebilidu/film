from django.db import models
import datetime

class Country(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Director(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200) 

    def __str__(self):
        return f"{self.first_name} {self.last_name}" 


class Film(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField(default=datetime.date.today)
    created_in_country = models.ForeignKey(Country, on_delete=models.PROTECT)
    available_in_countries = models.ManyToManyField(Country, related_name = 'available_in_countries')
    category = models.ManyToManyField(Category, related_name = 'categories')
    director = models.ManyToManyField(Director, related_name = 'directors')

    def __str__(self):
        return self.title
