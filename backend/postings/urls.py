from django.urls import path

from postings.views import (
    FreeBoardListView,
    FreeBoardDetailView,
    FreeBoardCommentView,
    FreeBoardView,
)

urlpatterns = [
    path("freeboards", FreeBoardListView.as_view()),
    path("freeboards/detail", FreeBoardDetailView.as_view()),
    path("freeboards/detail/<int:posting_id>", FreeBoardDetailView.as_view()),
    path("freeboards/comment", FreeBoardCommentView.as_view()),
    path("freeboards/view", FreeBoardView.as_view()),
]

