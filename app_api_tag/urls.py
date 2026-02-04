from django.urls import path 
from . import views 

urlpatterns = [
    path("create/", views.create_tag),
    path("display/", views.display_all_tags),
    path("delete/<int:id>/", views.delete_tag),
]
