from django.urls import path

from postings.views import (
    OperatingListView,
    OperatingDetailView,
    OperatingCommentView,
    FreeBoardListView,
    FreeBoardDetailView,
    FreeBoardCommentView,
    NoticeListView,
    NoticeDetailView,
    NoticeCommentView,
)

urlpatterns = [
    # 운영 게시판
    path("operatings", OperatingListView.as_view()),
    path("operatings/detail/<int:posting_id>", OperatingDetailView.as_view()),
    path("operatings/comment", OperatingCommentView.as_view()),

    # 자유게시판
    path("freeboards", FreeBoardListView.as_view()),
    path("freeboards/detail/<int:posting_id>", FreeBoardDetailView.as_view()),
    path("freeboards/comment", FreeBoardCommentView.as_view()),

    # 공지사항
    path("notices", NoticeListView.as_view()),
    path("notices/detail/<int:posting_id>", NoticeDetailView.as_view()),
    path("notices/comment", NoticeCommentView.as_view())
]
