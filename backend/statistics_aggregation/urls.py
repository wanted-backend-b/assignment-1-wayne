from django.urls import path
from .views import FreeGenderView, NoticeGenderView, OperateAgeView
from .views import OperateGenderView, NoticeAgeView, FreeAgeView
from .views import OperateTimeView, NoticeTimeView, FreeTimeView

urlpatterns = [
    path("gender/operate/", OperateGenderView.as_view()),
    path("gender/notice/", NoticeGenderView.as_view()),
    path("gender/free/", FreeGenderView.as_view()),
    path("age/operate/", OperateAgeView.as_view()),
    path("age/notice/", NoticeAgeView.as_view()),
    path("age/free/", FreeAgeView.as_view()),
    path("time/operate/", OperateTimeView.as_view()),
    path("time/notice/", NoticeTimeView.as_view()),
    path("time/free/", FreeTimeView.as_view()),
]
