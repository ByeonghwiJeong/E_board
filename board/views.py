import json

from django.views import View
from django.http import JsonResponse

from eboard.utils import login_decorator

from users.models import User
from .models import Notice


class NoticePostView(View):
    @login_decorator
    def post(self, request):
        try:
            user = request.user
            print(user.id)

            if not user.authorization == 2:
                return JsonResponse({'Message': 'unauthorized'}, status = 401)

            data    = json.loads(request.body)
            title   = data['title']
            content = data['content']

            Notice.objects.create(
                user_id    = user.id,
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
                'title': notice.title,
                'writer': notice.user.name,
                'content': notice.content
            }
            return JsonResponse({'results': notice_detail}, status = 200)

        except Notice.DoesNotExist:
            return JsonResponse({'Message': 'DOES_NOT_EXIST'}, status = 400)            