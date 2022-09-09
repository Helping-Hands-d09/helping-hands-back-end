from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("api/v1/users/", include("accounts.urls")),
    path("api/v1/campaign/", include("campaign.urls")),

    path("api-auth/", include("rest_framework.urls")),
]