# filepath: /c:/Users/mhdaz/LittleCouture/LittleCouture/fashion/admin.py
from django.contrib import admin
from .models import Category, Article, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Article)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    
admin.site.register(Category)
#admin.site.register(Article)
admin.site.register(Comment)
