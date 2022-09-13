from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import ProductModel


@receiver(pre_save, sender=ProductModel)
def get_real_price(sender, inctance, *args,**kwargs):

    if inctance.is_discount:
        inctance.real_price = ((100 - inctance.discount) / 100) * inctance.price
    else:
        inctance.real_price = inctance.price