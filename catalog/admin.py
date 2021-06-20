from django.contrib import admin
from .models import Client, Vozvrat, Oborudovanie

# Register your models here.

admin.site.register(Client)
admin.site.register(Vozvrat)
admin.site.register(Oborudovanie)