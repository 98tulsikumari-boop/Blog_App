from django.urls import path 
from . import views 

urlpatterns = [
    path("add/", views.add_bookmark),
    path("remove/<int:blog_id>/", views.remove_bookmark),
    path("all/", views.get_user_bookmarks),
    path("check/<int:blog_id>/", views.check_bookmark)
]
