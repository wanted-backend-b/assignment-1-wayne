from django.http import JsonResponse
from django.views.generic import View
from postings.models import FreeView, NoticeView, OperatingView
from rest_framework import status


class OperateGenderView(View):
    def get(self, request):
        male_num = (
            OperatingView.objects.select_related("user")
            .filter(user__gender="m")
            .distinct()
            .values_list("user")
            .count()
        )
        female_num = (
            OperatingView.objects.select_related("user")
            .filter(user__gender="f")
            .distinct()
            .values_list("user")
            .count()
        )

        result = {"M": male_num, "F": female_num}

        return JsonResponse({"result": result}, status=status.HTTP_200_OK)


class NoticeGenderView(View):
    def get(self, request):
        male_num = (
            NoticeView.objects.select_related("user")
            .filter(user__gender="m")
            .distinct()
            .values_list("user")
            .count()
        )
        female_num = (
            NoticeView.objects.select_related("user")
            .filter(user__gender="f")
            .distinct()
            .values_list("user")
            .count()
        )

        result = {"M": male_num, "F": female_num}

        return JsonResponse({"result": result}, status=status.HTTP_200_OK)


class FreeGenderView(View):
    def get(self, request):
        male_num = (
            FreeView.objects.select_related("user")
            .filter(user__gender="m")
            .distinct()
            .values_list("user")
            .count()
        )
        female_num = (
            FreeView.objects.select_related("user")
            .filter(user__gender="f")
            .distinct()
            .values_list("user")
            .count()
        )

        result = {"M": male_num, "F": female_num}

        return JsonResponse({"result": result}, status=status.HTTP_200_OK)


class OperateAgeView(View):
    def get(self, request):

        result = {}

        for i in range(1, 10):
            age_num = (
                OperatingView.objects.select_related("user")
                .filter(user__age__gte=i * 10, user__age__lt=i * 10 + 10)
                .distinct()
                .values_list("user")
                .count()
            )
            age_key = str(i * 10)

            result[age_key] = age_num

        return JsonResponse(result, status=status.HTTP_200_OK)


class NoticeAgeView(View):
    def get(self, request):

        result = {}

        for i in range(1, 10):
            age_num = (
                NoticeView.objects.select_related("user")
                .filter(user__age__gte=i * 10, user__age__lt=i * 10 + 10)
                .distinct()
                .values_list("user")
                .count()
            )
            age_key = str(i * 10)

            result[age_key] = age_num

        return JsonResponse(result, status=status.HTTP_200_OK)


class FreeAgeView(View):
    def get(self, request):

        result = {}

        for i in range(1, 10):
            age_num = (
                FreeView.objects.select_related("user")
                .filter(user__age__gte=i * 10, user__age__lt=i * 10 + 10)
                .distinct()
                .values_list("user")
                .count()
            )
            age_key = str(i * 10)

            result[age_key] = age_num

        return JsonResponse(result, status=status.HTTP_200_OK)
