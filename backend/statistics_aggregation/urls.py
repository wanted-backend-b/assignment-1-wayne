from django.urls import path
from .views import FreeGenderView, NoticeGenderView, OperateGenderView

urlpatterns = [
    path('gender/operate/', OperateGenderView.as_view()),
    path('gender/notice/', NoticeGenderView.as_view()),
    path('gender/free/', FreeGenderView.as_view()),

]
