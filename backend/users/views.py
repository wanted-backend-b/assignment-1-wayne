import json, jwt, bcrypt

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from .models import User


class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            name = data['name']
            email = data['email']
            password = data['password']

            if User.objects.filter(email=email).exists():
                return JsonResponse({'message': '이미 있는 이메일입니다.'}, status=400)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            decode_password = hashed_password.decode('utf-8')

            User.objects.create(
                name=name,
                email=email,
                password=decode_password
            )

            return JsonResponse({'message': 'success'}, status=201)

        except:
            return JsonResponse({'message': 'error'}, status=400)
