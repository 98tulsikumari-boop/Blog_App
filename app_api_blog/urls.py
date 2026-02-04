from django.urls import path
from . import views 

urlpatterns = [
    # For Blog APIs
    path("create/", views.create_blog),
    path("display/", views.display_all_blog),
    path("display/<int:id>/", views.display_blog),
    path("Update_put_api/<int:id>/", views.Update_put_api),
    path("delete/<int:id>/", views.delete_blog),
    path("blog_search/", views.filter_blogs),
    
]
