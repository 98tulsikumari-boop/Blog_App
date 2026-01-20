from django.urls import path
from . import views 

urlpatterns = [
    
    # For Tag APIs
    path("tag/", views.create_tag),
    path("tag/display/", views.display_all_tags),
    path("tag/delete/<int:id>/", views.delete_tag),
]
