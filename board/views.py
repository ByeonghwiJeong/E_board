import json

from django.views import View
from django.http import JsonResponse

from eboard.utils import login_decorator

from users.models import User
from .models import AdminBoard, Notice, FreeBoard


class NoticePostView(View):
    @login_decorator
    def post(self, request):
        try:
            user = request.user

            if not user.authorization == 2:
                return JsonResponse({'Message': 'unauthorized'}, status = 401)

            data    = json.loads(request.body)
            title   = data['title']
            content = data['content']

            Notice.objects.create(
                user_id = user.id,
                title   = title,
                content = content
            )

            return JsonResponse({'Message': 'SUCCESS'}, status = 200)
        except KeyError:
            return JsonResponse({'Message': 'KEY_ERROR'}, status = 400)

class NoticeView(View):
    def get(self, request, notice_id):
        try:
            notice = Notice.objects.get(id = notice_id)
            notice_detail = {
                'title'  : notice.title,
                'writer' : notice.user.name,
                'content': notice.content
            }

            return JsonResponse({'results': notice_detail}, status = 200)
        except Notice.DoesNotExist:
            return JsonResponse({'Message': 'DOES_NOT_EXIST'}, status = 400)


class AdminBoardPostView(View):
    @login_decorator
    def post(self, request):
        try:
            user = request.user

            if not user.authorization == 2:
                return JsonResponse({'Message': 'unauthorized'}, status = 401)

            data    = json.loads(request.body)
            title   = data['title']
            content = data['content']

            AdminBoard.objects.create(
                user_id = user.id,
                title   = title,
                content = content
            )

            return JsonResponse({'Message': 'SUCCESS'}, status = 200)
        except KeyError:
            return JsonResponse({'Message': 'KEY_ERROR'}, status = 400)

class AdminBoardView(View):
    @login_decorator
    def get(self, request, adminboard_id):
        try:
            user = request.user

            if not user.authorization == 2:
                return JsonResponse({'Message': 'unauthorized'}, status = 401)

            adminboard = AdminBoard.objects.get(id = adminboard_id)
            adminboard_detail = {
                'title'  : adminboard.title,
                'writer' : adminboard.user.name,
                'content': adminboard.content
            }

            return JsonResponse({'results': adminboard_detail}, status = 200)
        except AdminBoard.DoesNotExist:
            return JsonResponse({'Message': 'DOES_NOT_EXIST'}, status = 400)


class FreeBoardPostView(View):
    @login_decorator
    def post(self, request):
        try:
            user = request.user

            if not user.authorization >= 1:
                return JsonResponse({'Message': 'unauthorized'}, status = 401)

            data    = json.loads(request.body)
            title   = data['title']
            content = data['content']

            FreeBoard.objects.create(
                user_id = user.id,
                title   = title,
                content = content
            )

            return JsonResponse({'Message': 'SUCCESS'}, status = 200)
        except KeyError:
            return JsonResponse({'Message': 'KEY_ERROR'}, status = 400)

class FreeBoardView(View):
    def get(self, request, freeboard_id):
        try:

            freeboard = FreeBoard.objects.get(id = freeboard_id)
            freeboard_detail = {
                'title'  : freeboard.title,
                'writer' : freeboard.user.name,
                'content': freeboard.content
            }

            return JsonResponse({'results': freeboard_detail}, status = 200)
        except FreeBoard.DoesNotExist:
            return JsonResponse({'Message': 'DOES_NOT_EXIST'}, status = 400)  