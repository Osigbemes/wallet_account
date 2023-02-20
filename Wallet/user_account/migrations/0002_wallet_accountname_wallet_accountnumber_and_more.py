# Generated by Django 4.0 on 2023-02-20 20:39

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='accountName',
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='wallet',
            name='accountNumber',
            field=models.CharField(max_length=10, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AddField(
            model_name='wallet',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=30),
        ),
        migrations.AddField(
            model_name='wallet',
            name='transactionType',
            field=models.CharField(blank=True, choices=[('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='wallet',
            name='transaction_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='wallet',
            name='transaction_history',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='wallet',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_account.useraccount'),
        ),
    ]