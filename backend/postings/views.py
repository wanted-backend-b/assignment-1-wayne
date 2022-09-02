import json

from django.views import View
from django.http  import JsonResponse

from .models import NoticeBoardPosting, NoticeComment, NoticeView
from users.utils import login_deco


class NoticeBoardListView(View):
    """
    * @code writer 조현우
    * @GET ("/postings/notices")
    *
    * @returns json
    """

    @login_deco
    def get(self, request):
        postings = NoticeBoardPosting.objects.all()

        results = [{
            'id'      : posting.id,
            'title'   : posting.title,
            'context' : posting.context[:15],
            'views'   : NoticeView.objects.filter(notice_posting=posting).count()
        } for posting in postings ]

        return JsonResponse({'results' : results}, status = 200)


class NoticeDetailView(View):
    """
    * @code writer 조현우
    * @GET ("/postings/notices/detail")
    *
    * @returns json
    """
    def get(self, request, posting_id):
        try:
            posting = NoticeBoardPosting.objects.get(id=posting_id)
            comments = NoticeComment.objects.filter(notice_posting=posting)

            result = {
                'id'       : posting.id,
                'title'    : posting.title,
                'context'  : posting.context,
                'views'    : NoticeView.objects.filter(notice_posting=posting).count(),
                'comments' : [comment for comment in comments]
            }

            return JsonResponse({'result' : result}, status = 200)
        except NoticeBoardPosting.DoesNotExist:
            return JsonResponse({'message' : 'POSTING_DOES_NOT_EXIST'}, status = 400)

    """
    * @code writer 조현우
    * @POST ("/postings/freeboards/detail/<int:posting_id>")
    *
    * @returns json
    """
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user

            if user.level != 2:
                return JsonResponse({'message' : 'NO_AUTHENTIFICATION'}, status = 403)

            posting, is_created = NoticeBoardPosting.objects.update_or_create(
                title    = data['title'],
                context  = data['context'],
                defaults = {
                    'title'   : data['title'],
                    'context' : data['context']
                }
            )

            status_code = 201 if is_created else 200
            return JsonResponse({'message' : 'SUCCESS'}, status = status_code)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

    """
    * @code writer 조현우
    * @DELETE ("/postings/notices/detail")
    *
    * @returns json
    """
    def delete(self, request):
        try:
            data = json.loads(request)
            user = request.user

            if user.level != 2:
                return JsonResponse({'message' : 'NO_AUTHENTIFICATION'}, status = 403)

            posting = NoticeBoardPosting.objects.get(id=data["posting_id"])
            posting.delete()

            return JsonResponse({'message' : 'DATA_DELETED'}, status = 204)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
        except NoticeBoardPosting.DoesNotExist:
            return JsonResponse({'message' : 'POSTING_DOES_NOT_EXIST'}, status = 400)