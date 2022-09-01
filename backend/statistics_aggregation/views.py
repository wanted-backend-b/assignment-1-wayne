from django.http import JsonResponse
from django.views.generic import View
from postings.models import FreeView, NoticeView, OperatingView
from rest_framework import status


class OperateGenderView(View):
    def get(self, request):
        male_num = OperatingView.objects.select_related('user').\
                    filter(user__gender='m').count()
        female_num = OperatingView.objects.select_related('user').\
                      filter(user__gender='f').count()

        result = {
            "M": male_num,
            "F": female_num
        }

        return JsonResponse({'result': result}, status=status.HTTP_200_OK)


class NoticeGenderView(View):
    def get(self, request):
        male_num = NoticeView.objects.select_related('user').\
                    filter(user__gender='m').count()
        female_num = NoticeView.objects.select_related('user').\
                      filter(user__gender='f').count()

        result = {
            "M": male_num,
            "F": female_num
        }

        return JsonResponse({'result': result}, status=status.HTTP_200_OK)


class FreeGenderView(View):
    def get(self, request):
        male_num = FreeView.objects.select_related('user').\
                    filter(user__gender='m').count()
        female_num = FreeView.objects.select_related('user').\
                      filter(user__gender='f').count()

        result = {
            "M": male_num,
            "F": female_num
        }

        return JsonResponse({'result': result}, status=status.HTTP_200_OK)