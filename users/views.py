import json
import re
import bcrypt
import jwt

from django.views import View
from django.http import JsonResponse
from django.conf import settings

from eboard.utils import login_decorator

from .models import User

class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            name     = data['name']
            email    = data['email']
            password = data['password']
            phone    = data['phone']
            gender   = data['gender']
            age      = data['age']

            REX_EMAIL = "^[a-zA-Z0-9.-_+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$"

            if User.objects.filter(email = email).exists():
                return JsonResponse({'Message': 'Email_Already_Exist'}, status=400)
            
            if not re.match(REX_EMAIL, email):
                return JsonResponse({"Message": "INVALID_EMAIL"}, status=400)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                name     = name,
                email    = email,
                password = hashed_password,
                phone    = phone,
                gender   = gender,
                age      = age
            )

            return JsonResponse({'Message': 'SUCCESS'}, status = 201)

        except KeyError:
            return JsonResponse({'Message': 'KEY_ERROR'}, status = 400)

class LoginView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = User.objects.get(email = data['email'])

            if not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({"message" : "INVALID_PASSWORD"}, status=401)

            access_token = jwt.encode({"id" : user.id}, settings.SECRET_KEY, algorithm = settings.ALGORITHM)

            return JsonResponse({
                "message"      : "SUCCESS",     
                "access_token" : access_token
            }, status=200)

        except KeyError:
            return JsonResponse({'Message': 'KEY_ERROR'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"message" : "INVALID_ACCOUNT"}, status=404)


class WithdrawView(View):
    @login_decorator
    def post(self, request):
        user = request.user
        user.delete()
        return JsonResponse({"message": "Withdraw_SUCCESS"}, status = 200)