import json

from django.views import View
from django.http import JsonResponse

from postings.models import (
    OperatingBoardPosting,
    OperatingComment,
    OperatingView,
    FreeBoardPosting,
    FreeComment,
    FreeView,
    NoticeBoardPosting,
    NoticeComment,
    NoticeView
)
from core.utils      import login_deco


class FreeBoardListView(View):
    """
    * @code writer 조현우
    * @GET ("/postings/freeboards")
    *
    * @returns json
    """
    @login_deco
    def get(self, request):
        user = request.user
        postings = FreeBoardPosting.objects.all()

        results = [
            {
                "id": posting.id,
                "title": posting.title,
                "context": posting.context,
                "views": FreeView.objects.filter(free_board_posting=posting).count(),
            }
            for posting in postings
        ]

        return JsonResponse({"results": results}, status=200)

    """
    * @code writer 김대휘
    * @GET ("/postings/freeboards")
    * @description 자유 게시판 상세 생성
    * @returns json
    """
    @login_deco
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user

            FreeBoardPosting.objects.create(
                title=data["title"],
                context=data["context"],
                user=user
            )

            return JsonResponse({"message": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)


class FreeBoardDetailView(View):
    """
    * @code writer 조현우
    * @GET ("/postings/freeboards/detail")
    *
    * @returns json
    """

    @login_deco
    def get(self, request, posting_id):
        try:
            user = request.user

            posting = FreeBoardPosting.objects.get(id=posting_id)
            comments = FreeComment.objects.filter(free_board_posting=posting)

            FreeView.objects.create(
                free_board_posting = posting,
                user           = user
            )
            views = FreeView.objects.filter(free_board_posting=posting).count()

            result = {
                "id": posting.id,
                "title": posting.title,
                "context": posting.context,
                "views": views,
                "comments": [comment for comment in comments]
            }
            return JsonResponse({"result": result}, status=200)

        except FreeBoardPosting.DoesNotExist:
            return JsonResponse({"message": "POSTING_DOES_NOT_EXIST"}, status=400)

    """
    * @code writer 조현우
    * @POST ("/postings/freeboards/detail/<int:posting_id>")
    *
    * @returns json
    """
    @login_deco
    def put(self, request, posting_id):
        try:
            data       = json.loads(request.body)
            update_posting = FreeBoardPosting.objects.get(id=posting_id)

            if "title" in data:
                update_posting.title = data["title"]
            if "context" in data:
                update_posting.context = data["context"]
            update_posting.save()

            return JsonResponse({"message": "SUCCESS"}, status=200)

        except FreeBoardPosting.DoesNotExist as e:
            return JsonResponse({"message": str(e)}, status=400)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

    """
    * @code writer 조현우
    * @DELETE ("/postings/freeboards/detail")
    *
    * @returns json
    """

    @login_deco
    def delete(self, request, posting_id):
        try:
            user = request.user

            posting = FreeBoardPosting.objects.get(id=posting_id)

            if user != posting.user:
                return JsonResponse({"message": "NO_AUTHENTIFICATION"}, status=403)

            posting.delete()

            return JsonResponse({"message": "DATA_DELETED"}, status=204)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        except FreeBoardPosting.DoesNotExist:
            return JsonResponse({"message": "POSTING_DOES_NOT_EXIST"}, status=400)


class FreeBoardCommentView(View):
    """
    * @code writer 조현우
    * @POST ("/postings/freeboards/comment")
    *
    * @returns json
    """

    @login_deco
    def post(self, request):
        try:
            data       = json.loads(request.body)
            user       = request.user
            comment_id = request.GET.get("comment_id", None)
            posting    = FreeBoardPosting.objects.get(id=data['posting_id'])

            if FreeBoardPosting.objects.filter(id=comment_id).exists():
                FreeBoardPosting.objects.filter(id=comment_id).update(
                    comment         = data['comment']
                )
                return JsonResponse({"message": "SUCCESS"}, status=201)

            FreeComment.objects.create(
                comment         = data['comment'],
                free_board_posting  = posting,
                user            = user,
            )
            return JsonResponse({'message' : 'SUCCESS'}, status = 201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)


class OperatingListView(View):
    """
    * @code writer 조현우
    * @GET ("/postings/operatings")
    *
    * @returns json
    """
    @login_deco
    def get(self, request):
        user = request.user

        if user.level != "2":
            return JsonResponse({"message": "NO_AUTHENTIFICATION"}, status=403)
        
        postings = OperatingBoardPosting.objects.all()

        results = [
            {
                "id": posting.id,
                "title": posting.title,
                "context": posting.context,
                "views": OperatingView.objects.filter(
                    operating_board_posting=posting
                ).count(),
            }
            for posting in postings
        ]

        return JsonResponse({"results": results}, status=200)

    """
    * @code writer 김대휘
    * @GET ("/postings/freeboards")
    * @description 자유 게시판 상세 생성
    * @returns json
    """
    @login_deco
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user

            if user.level != "2":
                return JsonResponse({"message": "NO_AUTHENTIFICATION"}, status=403)

            OperatingBoardPosting.objects.create(
                title=data["title"],
                context=data["context"],
                user=user
            )

            return JsonResponse({"message": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)


class OperatingDetailView(View):
    """
    * @code writer 조현우
    * @GET ("/postings/operatings/detail")
    *
    * @returns json
    """
    @login_deco
    def get(self, request, posting_id):
        try:
            user = request.user

            if user.level != "2":
                return JsonResponse({"message": "NO_AUTHENTIFICATION"}, status=403)

            posting = OperatingBoardPosting.objects.get(id=posting_id)
            comments = OperatingComment.objects.filter(operating_board_posting=posting)

            OperatingView.objects.create(
                operating_board_posting  = posting,
                user                     = user
            )
            views = OperatingView.objects.filter(operating_board_posting=posting).count()

            result = {
                "id": posting.id,
                "title": posting.title,
                "context": posting.context,
                "views": views,
                "comments": [comment for comment in comments]
            }

            return JsonResponse({"result": result}, status=200)
        except OperatingBoardPosting.DoesNotExist:
            return JsonResponse({"message": "POSTING_DOES_NOT_EXIST"}, status=400)

    """
    * @code writer 조현우
    * @POST ("/postings/operatings/detail/<int:posting_id>")
    * @description 운영게시판 상세 생성
    * @returns json
    """
    @login_deco
    def put(self, request, posting_id):
        try:
            data       = json.loads(request.body)
            user       = request.user

            if user.level != "2":
                return JsonResponse({"message": "NO_AUTHENTIFICATION"}, status=403)

            update_operating_posting = OperatingBoardPosting.objects.get(id=posting_id)
            if "title" in data:
                update_operating_posting.title = data["title"]
            if "context" in data:
                update_operating_posting.context = data["context"]
            update_operating_posting.save()

            return JsonResponse({"message": "SUCCESS"}, status=200)

        except OperatingBoardPosting.DoesNotExist as e:
            return JsonResponse({"message": str(e)}, status=400)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

    """
    * @code writer 조현우
    * @DELETE ("/postings/operatings/detail/<int:posting_id>")
    *
    * @returns json
    """
    @login_deco
    def delete(self, request, posting_id):
        try:
            user = request.user

            if user.level != "2":
                return JsonResponse({"message": "NO_AUTHENTIFICATION"}, status=403)
            posting = OperatingBoardPosting.objects.get(id=posting_id)

            if user != posting.user:
                return JsonResponse({"message": "NO_AUTHENTIFICATION"}, status=403)

            posting.delete()

            return JsonResponse({"message": "DATA_DELETED"}, status=204)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        except OperatingBoardPosting.DoesNotExist:
            return JsonResponse({"message": "POSTING_DOES_NOT_EXIST"}, status=400)


class OperatingCommentView(View):
    """
    * @code writer 조현우
    * @POST ("/postings/operatings/comment")
    *
    * @returns json
    """
    @login_deco
    def post(self, request):
        try:
            data    = json.loads(request.body)
            user    = request.user
            posting = OperatingBoardPosting.objects.get(id=data['posting_id']) 

            if user.level != "2":
                return JsonResponse({"message": "NO_AUTHENTIFICATION"}, status=403)

            posting, is_created = OperatingComment.objects.update_or_create(
                comment                  = data['comment'],
                operating_board_posting  = posting,
                user                     = user,
                defaults = {
                    'comment' : data['comment']
                }
            )

            status_code = 201 if is_created else 200
            return JsonResponse({'message' : 'SUCCESS'}, status = status_code)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)


class NoticeListView(View):
    """
    * @code writer 조현우
    * @GET ("/postings/notices")
    *
    * @returns json
    """

    @login_deco
    def get(self, request):
        user = request.user

        postings = NoticeBoardPosting.objects.all()

        results = [
            {
                "id": posting.id,
                "title": posting.title,
                "context": posting.context[:15],
                "views": NoticeView.objects.filter(
                    notice_posting=posting
                ).count(),
            }
            for posting in postings
        ]

        return JsonResponse({"results": results}, status=200)

    """
    * @code writer 김대휘
    * @POST ("/postings/notices")
    * @description 공지사항 게시판 생성
    * @returns message
    """
    @login_deco
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user

            if user.level != "2":
                return JsonResponse({"message": "NO_AUTHENTIFICATION"}, status=403)

            NoticeBoardPosting.objects.create(
                title=data["title"],
                context=data["context"],
                user=user
            )

            return JsonResponse({"message": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)


class NoticeDetailView(View):
    """
    * @code writer 조현우
    * @GET ("/postings/notices/detail")
    *
    * @returns json
    """
    @login_deco
    def get(self, request, posting_id):
        try:
            user = request.user

            posting = NoticeBoardPosting.objects.get(id=posting_id)
            comments = NoticeComment.objects.filter(notice_posting=posting)

            NoticeView.objects.create(
                notice_posting=posting,
                user=user
            )
            views = NoticeView.objects.filter(notice_posting=posting).count()

            result = {
                "id": posting.id,
                "title": posting.title,
                "context": posting.context,
                "views": views,
                "comments": [comment for comment in comments]
            }

            return JsonResponse({"result": result}, status=200)
        except NoticeBoardPosting.DoesNotExist:
            return JsonResponse({"message": "POSTING_DOES_NOT_EXIST"}, status=400)

    """
    * @code writer 조현우
    * @POST ("/postings/notices/detail/<int:posting_id>")
    * @description 공지사항 게시판 수정
    * @returns json
    """
    @login_deco
    def put(self, request, posting_id):
        try:
            data = json.loads(request.body)
            user = request.user

            if user.level != "2":
                return JsonResponse({"message": "NO_AUTHENTIFICATION"}, status=403)

            update_notice_posting = NoticeBoardPosting.objects.get(id=posting_id)
            if "title" in data:
                update_notice_posting.title = data["title"]
            if "context" in data:
                update_notice_posting.context = data["context"]
            update_notice_posting.save()

            return JsonResponse({"message": "SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

    """
    * @code writer 조현우
    * @DELETE ("/postings/notices/detail/<int:posting_id>")
    *
    * @returns json
    """
    @login_deco
    def delete(self, request, posting_id):
        try:
            user = request.user

            if user.level != "2":
                return JsonResponse({"message": "NO_AUTHENTIFICATION"}, status=403)

            posting = NoticeBoardPosting.objects.get(id=posting_id)

            if user != posting.user:
                return JsonResponse({"message": "NO_AUTHENTIFICATION"}, status=403)

            posting.delete()

            return JsonResponse({"message": "DATA_DELETED"}, status=204)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        except NoticeBoardPosting.DoesNotExist:
            return JsonResponse({"message": "POSTING_DOES_NOT_EXIST"}, status=400)


class NoticeCommentView(View):
    """
    * @code writer 조현우
    * @POST ("/postings/notices/comment")
    *
    * @returns json
    """

    @login_deco
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user
            comment_id = request.GET.get("comment_id", None)
            posting = NoticeBoardPosting.objects.get(id=data['posting_id'])

            if user.level != "2":
                return JsonResponse({"message": "NO_AUTHENTIFICATION"}, status=403)

            if NoticeBoardPosting.objects.filter(id=comment_id).exists():
                NoticeBoardPosting.objects.filter(id=comment_id).update(
                    comment=data['comment']
                )

                return JsonResponse({"message": "SUCCESS"}, status=201)

            NoticeComment.objects.create(
                comment=data['comment'],
                notice_posting=posting,
                user=user,
            )

            return JsonResponse({'message': 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)