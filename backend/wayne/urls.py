from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("postings", include("postings.urls")),
    path("statistics", include('statistics_aggregation.urls')),
    path("users", include("users.urls")),
]
