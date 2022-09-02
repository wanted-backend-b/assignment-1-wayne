import json

from django.views  import View
from django.http   import JsonResponse

from postings.models import FreeBoardPosting, FreeComment, FreeView
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

        results = [{
            'id'      : posting.id,
            'title'   : posting.title,
            'context' : posting.context[:15],
            'views'   : FreeView.objects.filter(free_board_posting=posting).count()
        } for posting in postings ]

        return JsonResponse({'results' : results}, status = 200)


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

            result = {
                'id'       : posting.id,
                'title'    : posting.title,
                'context'  : posting.context,
                'views'    : FreeView.objects.filter(free_board_posting=posting).count(),
                'comments' : [comment.comment for comment in comments]
            }

            return JsonResponse({'result' : result}, status = 200)
        except FreeBoardPosting.DoesNotExist:
            return JsonResponse({'message' : 'POSTING_DOES_NOT_EXIST'}, status = 400)

    """
    * @code writer 조현우
    * @POST ("/postings/freeboards/detail/<int:posting_id>")
    *
    * @returns json
    """
    @login_deco
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user

            posting, is_created = FreeBoardPosting.objects.update_or_create(
                title    = data['title'],
                context  = data['context'],
                user     = user,
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
    * @DELETE ("/postings/freeboards/detail")
    *
    * @returns json
    """
    @login_deco
    def delete(self, request):
        try:
            data = json.loads(request)
            user = request.user

            if user.level != 2:
                return JsonResponse({'message' : 'NO_AUTHENTIFICATION'}, status = 403)

            posting = FreeBoardPosting.objects.get(id=data["posting_id"])
            posting.delete()

            return JsonResponse({'message' : 'DATA_DELETED'}, status = 204)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
        except FreeBoardPosting.DoesNotExist:
            return JsonResponse({'message' : 'POSTING_DOES_NOT_EXIST'}, status = 400) 