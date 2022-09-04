import os
import jwt

from django.http import JsonResponse

from users.models import User


def login_deco(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            token = request.headers.get("Authorization", None)
            token_payload = jwt.decode(
                token, os.environ.get("SECRET"), os.environ.get("ALGORITHM")
            )
            user = User.objects.get(id=token_payload["user_id"])
            request.user = user

            return func(self, request, *args, **kwargs)

        except jwt.DecodeError:
            return JsonResponse({"message": "wrong user"}, status=401)

        except User.DoesNotExist:
            return JsonResponse({"message": "No User"}, status=401)

    return wrapper
