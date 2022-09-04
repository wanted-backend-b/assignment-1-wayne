from django.urls import path, include

urlpatterns = [
    path("postings/", include("postings.urls")),
    path("statistics/", include("statistics_aggregation.urls")),
    path("users/", include("users.urls")),
]
