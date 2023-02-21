from .views import BlacklistTokenUpdateView, DebitWalletAccount, GetAllWallets, GetWalletsByUser, RegisterAccount, Login, GetAllUsers, CreditWalletAccount
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register', RegisterAccount.as_view(), name="register"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    path('login/', Login.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get_users/', GetAllUsers.as_view(), name='get_users'),
    path('credit_wallet/', CreditWalletAccount.as_view(), name='credit_wallet'),
    path('debit_wallet/', DebitWalletAccount.as_view(), name='debit_wallet'),
    path('get_wallet_account/', GetAllWallets.as_view(), name='get_wallet_account'),
    path('get_wallet_by_user/', GetWalletsByUser.as_view(), name='get_wallet_by_user'),
]