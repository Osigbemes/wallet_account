from .views import RegisterAccount, Login
from django.urls import path

urlpatterns = [
    path('register', RegisterAccount.as_view(), name="register"),
    path('login', Login.as_view(), name="login"),
]