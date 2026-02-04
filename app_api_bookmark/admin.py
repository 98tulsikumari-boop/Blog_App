from django.contrib import admin
from .models import BookMark

# Register your models here.
@admin.register(BookMark)
class BookMarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'blog', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'blog__title']
