from django.urls import path
from users.views import SignupView, LoginView, WithdrawView

urlpatterns = [
    path('/signup', SignupView.as_view()),
    path('/login', LoginView.as_view()),
    path('/withdraw', WithdrawView.as_view()),
]