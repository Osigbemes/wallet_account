from django.contrib import admin
from .models import UserAccount, Wallet

admin.site.register(UserAccount)
admin.site.register(Wallet)