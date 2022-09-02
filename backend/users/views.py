import json, bcrypt, os, jwt

from django.views import View
from django.http import JsonResponse

from .models import User


class SignUpView(View):
    ''' 유저 회원가입 API '''
    def post(self, request):
        try:
            data = json.loads(request.body)
            name = data['name']
            email = data['email']
            password = data['psword']
            gender = data['gender']
            age = data['age']
            phone_number = data['phone_number']
            level = data['level']

            if User.objects.filter(email=email).exists():
                return JsonResponse({'message': '이미 있는 이메일입니다.'}, status=400)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            decode_password = hashed_password.decode('utf-8')

            User.objects.create(
                name=name,
                email=email,
                psword=decode_password,
                gender=gender,
                age=age,
                phone_number=phone_number,
                level=level
            )
            return JsonResponse({'message': '회원가입 완료'}, status=201)

        except Exception as e:
            print("error: ", e) # 에러 코드 확인
            return JsonResponse({'message': '회원가입 실패'}, status=400)

