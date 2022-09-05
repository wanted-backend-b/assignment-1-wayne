from django.urls import path

from postings.views import (
    NoticeListView,
    NoticeDetailView,
    NoticeCommentView,
)

urlpatterns = [
    path("/notices", NoticeListView.as_view()),
    path("/notices/detail", NoticeDetailView.as_view()),
    path("/notices/detail/<int:posting_id>", NoticeDetailView.as_view()),
    path("/notices/comment", NoticeCommentView.as_view())
]

