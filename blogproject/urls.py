
from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    # API endpoints
    path("api/v1/auth/", include("app_api_account.urls")),
    path("api/v1/category/", include("app_api_category.urls")),
    path("api/v1/tag/", include("app_api_tag.urls")),
    path("api/v1/blog/", include("app_api_blog.urls")),
    path("api/v1/bookmark/", include("app_api_bookmark.urls")),
    path("api/v1/subscribe/", include("app_api_newsletter.urls")), 
    path('api/v1/contact/',include('app_api_contact.urls'))

    # Template
    # path("category/", include("app_template_category")),
]

# Serve Media  files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

