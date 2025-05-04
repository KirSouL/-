from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.apps import UsersConfig
from users.views import UserRegistrateView, UserPasswordResetView, UserProfileView, email_verification

app_name = UsersConfig

urlpatterns = [
    path('', LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registrate_user/', UserRegistrateView.as_view(), name='create_user'),
    path('password_user/', UserPasswordResetView.as_view(), name='pass_user'),
    path('profile_user/', UserProfileView.as_view(), name='profile_user'),
    path('email_confirm//<str:token>/', email_verification, name='email_confirm'),
]
