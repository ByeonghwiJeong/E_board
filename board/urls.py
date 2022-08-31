from django.urls import path
from .views import NoticePostView, NoticeView, AdminBoard, AdminBoardPostView, FreeBoardPostView, FreeBoardView

urlpatterns = [
    path('/notice/post', NoticePostView.as_view()),
    path('/notice/<int:notice_id>', NoticeView.as_view()),
    path('/adminboard/post', AdminBoardPostView.as_view()),
    path('/adminboard/<int:adminboard_id>', AdminBoard.as_view()),
    path('/freeboard/post', FreeBoardPostView.as_view()),
    path('/freeboard/<int:freeboard_id>', FreeBoardView.as_view()),
]