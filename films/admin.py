from django.contrib import admin
from .models import Country, Category, Film, Director

admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Director)
admin.site.register(Film)