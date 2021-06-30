from django.contrib import admin
<<<<<<< HEAD
from .models import Country, Category, Film, Director

admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Director)
admin.site.register(Film)
=======
from .models import Country, Category, Director, Film

admin.site.register(Country)
admin.site.register(Category)
admin.site.register(Director)
admin.site.register(Film)
>>>>>>> f8cc9b8503b2e0b147baa2f24d5d11890618f4e6
