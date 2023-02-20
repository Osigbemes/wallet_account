from decimal import Decimal
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import MinLengthValidator

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, first_name, last_name, password, email, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(first_name, last_name, password, email, **other_fields)

    def create_user(self, first_name, last_name, email, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email'))

        user = self.model(first_name=first_name, email=email, last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    token = models.TextField(blank=True)
    objects = CustomAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
    
class Wallet(models.Model):
    TRANSACTIONTYPE=(
        ('Deposit', 'Deposit'),
        ('Withdrawal', 'Withdrawal')
    )

    transactionType=models.CharField(max_length=200, null=True, choices=TRANSACTIONTYPE, blank=True)
    account_number = models.CharField(validators=[MinLengthValidator(10)], unique=True, max_length=10, null=True)
    account_name = models.CharField(max_length=150, unique=True, null=True)
    amount = models.DecimalField(max_digits=30, decimal_places=2, default=Decimal(0.00))
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE, null=True, blank=True)
    transaction_date = models.DateTimeField(default=timezone.now)
    transaction_history = models.TextField(blank=True)

    def __str__(self):
        return self.user