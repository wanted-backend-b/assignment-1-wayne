import json

from django.views import View
from django.http import JsonResponse

from postings.models import OperatingBoardPosting, OperatingComment, OperatingView
from core.utils      import login_deco

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
                "context": posting.context[:15],
                "views": OperatingView.objects.filter(
                    operating_board_posting=posting
                ).count(),
            }
            for posting in postings
        ]

        return JsonResponse({"results": results}, status=200)


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
    *
    * @returns json
    """
    @login_deco
    def post(self, request):
        try:
            data       = json.loads(request.body)
            user       = request.user
            posting_id = data["posting_id"]

            if user.level != "2":
                return JsonResponse({"message": "NO_AUTHENTIFICATION"}, status=403)

            if OperatingBoardPosting.objects.filter(id=posting_id).exists():
                OperatingBoardPosting.objects.filter(id=posting_id).update(
                    title   = data["title"],
                    context = data["context"],
                )

                return JsonResponse({"message": "SUCCESS"}, status=201)

            OperatingBoardPosting.objects.create(
                title   = data["title"],
                context = data["context"],
                user    = user
            )

            return JsonResponse({"message": "SUCCESS"}, status=201)

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