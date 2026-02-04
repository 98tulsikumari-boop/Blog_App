from django.contrib import admin
from .models import Subscriber 

# Register your models here.
@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'subscribed_on', 'is_active']
    list_filter = ['is_active', 'subscribed_on']
    search_fields = ['email']