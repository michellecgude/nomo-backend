from django.contrib import admin

# Register your models here.
from .models import User, Events, Births, Deaths

admin.site.register((User, Events, Births, Deaths))