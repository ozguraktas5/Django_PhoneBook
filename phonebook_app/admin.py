from django.contrib import admin
from .models import Person, Category, Location

admin.site.register(Category)
admin.site.register(Person)
admin.site.register(Location)

