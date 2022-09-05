from django.http import JsonResponse
from django.views.generic import View
from postings.models import FreeView, NoticeView, OperatingView
from users.models import UpdatedTime
from rest_framework import status
from django.db.models import Q


"""
 * @code writer 전예솜
 * @description 운영게시판에 글을 등록한 사람의 남녀별 통계 집계 API 구현
 * @GET ("/statistics/gender/operate")
 * 
 * @returns json
 *
"""


class OperateGenderView(View):
    def get(self, request):
        male_num = (
            OperatingView.objects.select_related("user")
            .filter(
                Q(user__gender="m") | Q(user__gender="M") | Q(user__gender="남")
            )
            .distinct()
            .values_list("user")
            .count()
        )
        female_num = (
            OperatingView.objects.select_related("user")
            .filter(
                Q(user__gender="f") | Q(user__gender="F") | Q(user__gender="여")
            )
            .distinct()
            .values_list("user")
            .count()
        )

        result = {"M": male_num, "F": female_num}

        return JsonResponse({"result": result}, status=status.HTTP_200_OK)


"""
 * @code writer 전예솜
 * @description 공지사항에 글을 등록한 사람의 남녀별 통계 집계 API 구현
 * @GET ("/statistics/gender/notice")
 * 
 * @returns json
 *
"""


class NoticeGenderView(View):
    def get(self, request):
        male_num = (
            NoticeView.objects.select_related("user")
            .filter(
                Q(user__gender="m") | Q(user__gender="M") | Q(user__gender="남")
            )
            .distinct()
            .values_list("user")
            .count()
        )
        female_num = (
            NoticeView.objects.select_related("user")
            .filter(
                Q(user__gender="f") | Q(user__gender="F") | Q(user__gender="여")
            )
            .distinct()
            .values_list("user")
            .count()
        )

        result = {"M": male_num, "F": female_num}

        return JsonResponse({"result": result}, status=status.HTTP_200_OK)


"""
 * @code writer 전예솜
 * @description 자유게시판에 글을 등록한 사람의 남녀별 통계 집계 API 구현
 * @GET ("/statistics/gender/free")
 * 
 * @returns json
 *
"""


class FreeGenderView(View):
    def get(self, request):
        male_num = (
            FreeView.objects.select_related("user")
            .filter(
                Q(user__gender="m") | Q(user__gender="M") | Q(user__gender="남")
            )
            .distinct()
            .values_list("user")
            .count()
        )
        female_num = (
            FreeView.objects.select_related("user")
            .filter(
                Q(user__gender="f") | Q(user__gender="F") | Q(user__gender="여")
            )
            .distinct()
            .values_list("user")
            .count()
        )

        result = {"M": male_num, "F": female_num}

        return JsonResponse({"result": result}, status=status.HTTP_200_OK)


"""
 * @code writer 전예솜
 * @description 운영게시판에 글을 등록한 사람의 나이별 통계 집계 API 구현
 * @GET ("/statistics/age/operate")
 * 
 * @returns json
 *
"""


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


"""
 * @code writer 전예솜
 * @description 공지사항에 글을 등록한 사람의 나이별 통계 집계 API 구현
 * @GET ("/statistics/age/notice")
 * 
 * @returns json
 *
"""


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


"""
 * @code writer 전예솜
 * @description 자유게시판에 글을 등록한 사람의 나이별 통계 집계 API 구현
 * @GET ("/statistics/age/free")
 * 
 * @returns json
 *
"""


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


"""
 * @code writer 전예솜
 * @description 이용자가 운영게시판을 조회한 시간대의 통계 집계 API 구현
 * @GET ("/statistics/time/operate")
 * 
 * @returns json
 *
"""


class OperateTimeView(View):
    def get(self, request):
        result = {}

        for i in range(1, 25):
            result[str(i)] = 0

        id_list = (
            OperatingView.objects.select_related("user")
            .distinct()
            .values("user")
        )

        for i in id_list:

            update_time = (
                Updated_time.objects.filter(user_id=i["user"])
                .order_by("-modified_at")
                .first()
            )
            key = str(update_time.modified_at.hour)
            result[key] = result[key] + 1

        return JsonResponse(result, status=status.HTTP_200_OK)


"""
 * @code writer 전예솜
 * @description 이용자가 공지사항을 조회한 시간대의 통계 집계 API 구현
 * @GET ("/statistics/time/notice")
 * 
 * @returns json
 *
"""


class NoticeTimeView(View):
    def get(self, request):
        result = {}

        for i in range(1, 25):
            result[str(i)] = 0

        id_list = (
            NoticeView.objects.select_related("user").distinct().values("user")
        )

        for i in id_list:

            update_time = (
                Updated_time.objects.filter(user_id=i["user"])
                .order_by("-modified_at")
                .first()
            )
            key = str(update_time.modified_at.hour)
            result[key] = result[key] + 1

        return JsonResponse(result, status=status.HTTP_200_OK)


"""
 * @code writer 전예솜
 * @description 이용자가 자유게시판을 조회한 시간대의 통계 집계 API 구현
 * @GET ("/statistics/time/free")
 * 
 * @returns json
 *
"""


class FreeTimeView(View):
    def get(self, request):
        result = {}

        for i in range(1, 25):
            result[str(i)] = 0

        id_list = (
            FreeView.objects.select_related("user").distinct().values("user")
        )

        for i in id_list:

            update_time = (
                Updated_time.objects.filter(user_id=i["user"])
                .order_by("-modified_at")
                .first()
            )
            key = str(update_time.modified_at.hour)
            result[key] = result[key] + 1

        return JsonResponse(result, status=status.HTTP_200_OK)
