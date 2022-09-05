from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("postings/", include("postings.urls")),
    path("statistics/", include("statistics_aggregation.urls")),
    path("users/", include("users.urls")),
]
