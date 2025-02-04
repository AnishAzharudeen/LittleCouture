# filepath: /c:/Users/mhdaz/LittleCouture/LittleCouture/fashion/admin.py
from django.contrib import admin
from .models import Category, Article

admin.site.register(Category)
admin.site.register(Article)
