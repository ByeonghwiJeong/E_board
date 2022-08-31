from django.urls import path
from .views import NoticePostView, NoticeView

urlpatterns = [
    path('/notice/post', NoticePostView.as_view()),
    path('/notice/<int:notice_id>', NoticeView.as_view()),
    path('/adminboard/post', NoticePostView.as_view()),
    path('/adminboard/<int:adminboard_id>', NoticeView.as_view()),
]