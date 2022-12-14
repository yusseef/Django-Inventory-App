from django.contrib import admin
from .models import Articles
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'timestamp', 'updated']
    search_fields = ['title', 'content']
    raw_id_fields = ['user']

admin.site.register(Articles, ArticleAdmin)