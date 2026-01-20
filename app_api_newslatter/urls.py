from django.urls import path
from . import views

# For Newsletter APIs
urlpatterns = [
    path("subscribe_blog/", views.subscribe_blog),
    path("subscribers_list/", views.subscribers_list),
]
