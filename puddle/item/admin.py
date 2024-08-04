from django.contrib import admin

# Register your models here.
from .models import Category, Item
# untuk memunculkan tabel database, kita perlu meregister dulu di admin.py
admin.site.register(Category)
admin.site.register(Item)