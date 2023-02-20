
from django.db.models.signals import post_save, pre_delete, pre_save

from django.dispatch import receiver
from .models import Wallet, UserAccount


@receiver(post_save, sender=UserAccount)
def create_wallet_account(sender, instance, created, **kwargs):
    
    if created:
        Wallet.objects.create(user=instance)
       

@receiver(post_save, sender=UserAccount)
def save_profile(sender, instance, **kwargs):
		instance.wallet.save()
