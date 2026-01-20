
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("app_api_blog.urls")),
    path("", include("app_api_newslatter.urls")),
    path("category/", include("app_api_category.urls")),
]
