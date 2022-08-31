from django.urls import path
from .views import NoticePostView

urlpatterns = [
    path('/notice/post', NoticePostView.as_view()),
]