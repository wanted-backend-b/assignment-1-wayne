from django.urls import path

from postings.views import NoticeView

urlpatterns = [
    path("notices", FreeBoardListView.as_view()),
    path("notices/detail", FreeBoardDetailView.as_view()),
    path("notices/detail/<int:posting_id>", FreeBoardDetailView.as_view()),

]