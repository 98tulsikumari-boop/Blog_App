from django.urls import path 
from . import views 

urlpatterns = [
    # For Category APIs
    path("display/", views.categories_list),
    path("create/", views.create_category),
    path("update_put_api/<int:id>/", views.update_category),
    path("delete/<int:id>/", views.delete_category),
]
