from django.urls import path
from .views import UserLoginView, LogInSuccess, logout_view, UserSignUpView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('login_success/', LogInSuccess, name='login_success'),
    path('logout/', logout_view, name='logout'),
    path('signup/', UserSignUpView.as_view(), name='signup')
]