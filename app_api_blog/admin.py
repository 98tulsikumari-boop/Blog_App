from django.contrib import admin
from .models import Blog

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author_id', 'category', 'created_at']
    list_filter = ['category', 'tags', 'created_at']
    search_fields = ['title', 'content']
    filter_horizontal = ['tags']




