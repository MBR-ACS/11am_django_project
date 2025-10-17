from django.urls import path
from .views import signup
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('sign_up/', signup, name='sign-up'),
    path('log_in/', LoginView.as_view(), name='log-in'),
    path('log_out/', LogoutView.as_view(), name='log-out'),
]