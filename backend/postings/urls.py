from django.urls import path

from postings.views import NoticeView

urlpatterns = [
<<<<<<< HEAD
    path("freeboards", FreeBoardListView.as_view()),
    path("freeboards/detail", FreeBoardDetailView.as_view()),
    path("freeboards/detail/<int:posting_id>", FreeBoardDetailView.as_view()),
    
=======
    path("notices", FreeBoardListView.as_view()),
    path("notices/detail", FreeBoardDetailView.as_view()),
    path("notices/detail/<int:posting_id>", FreeBoardDetailView.as_view()),

>>>>>>> bf20324 (Feat: 공지사항 API 구현)
]