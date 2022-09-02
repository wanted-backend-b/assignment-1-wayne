import json, bcrypt, os, jwt

from django.views import View
from django.http import JsonResponse

from .models import User
from .utils import login_deco


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


class LogInView(View):
    ''' 유저 로그인 API '''
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data['email']
            password = data['psword']

            if not User.objects.filter(email=email).exists():
                return JsonResponse({"message": "이메일을 다시 입력하세요."}, status=401)

            user = User.objects.get(email=email)

            encoded_password = password.encode('utf-8')
            encoded_db_password = user.psword.encode('utf-8')

            if not bcrypt.checkpw(encoded_password, encoded_db_password):
                return JsonResponse({"message": "잘못된 비밀번호입니다."}, status=401)

            token = jwt.encode({'user_id': user.id}, os.environ.get("SECRET"), os.environ.get("ALGORITHM"))

            return JsonResponse({'token': token}, status=200)

        except Exception as e:
            print("error: ", e)
            return JsonResponse({'message': '로그인 실패'}, status=400)


class WithdrawalView(View):
    ''' 유저 회원탈퇴 API '''

    @login_deco
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data['email']
            password = data['psword']

            if not User.objects.filter(email=email).exists():
                return JsonResponse({"message": "이메일을 다시 입력하세요"}, status=401)

            user = User.objects.filter(email=email).first()

            encoded_password = password.encode('utf-8')
            encoded_db_password = user.psword.encode('utf-8')

            if not bcrypt.checkpw(encoded_password, encoded_db_password):
                return JsonResponse({"message": "잘못된 비밀번호입니다."}, status=401)

            if user:
                user.delete()
                return JsonResponse({"message":"회원탈퇴 완료"}, status=200)

        except Exception as e:
            print("error:", e)
            return JsonResponse({"message": "회원탈퇴 실패"}, status=400)

