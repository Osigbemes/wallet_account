# Generated by Django 4.0 on 2023-02-21 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0004_alter_wallet_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='transactionType',
            field=models.CharField(blank=True, choices=[('Debit', 'Debit'), ('Credit', 'Credit')], max_length=200, null=True),
        ),
    ]