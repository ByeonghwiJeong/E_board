import json
import re

from django.views import View
from django.http import JsonResponse
from django.conf import settings

from .models import User

class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            name = data['name']
            email = data['email']
            password = data['password']
            phone = data['phone']
            gender = data['gender']
            age = data['age']

            REX_EMAIL = "^[a-zA-Z0-9.-_+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$"

            if User.objects.filter(email = email).exists():
                return JsonResponse({'Message': 'Email_Already_Exist'}, status=400)
            
            if not re.match(REX_EMAIL, email):
                return JsonResponse({"Message": "Invalid_Email"}, status=400)

            User.objects.create(
                name = name,
                email = email,
                password = password,
                phone = phone,
                gender = gender,
                age = age
            )

            return JsonResponse({'Message': 'SUCCESS'}, status = 201)

        except KeyError:
            return JsonResponse({'Message': 'KEY_ERROR'}, status = 400)