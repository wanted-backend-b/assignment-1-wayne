from django.urls import path

from .views import NoticeBoardListView

urlpatterns = [
    path("freeboards/", NoticeBoardListView.as_view()),
    # path("freeboards/detail", FreeBoardDetailView.as_view()),
    # path("freeboards/detail/<int:posting_id>", FreeBoardDetailView.as_view()),
    
]