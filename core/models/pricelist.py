from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.urls import reverse


class PriceList(models.Model):
    name = models.CharField(max_length=256, default='')
    file = models.FileField(null=True)


@receiver(post_delete, sender=PriceList)
def promo_image_delete_handler(sender, **kwargs):
    instance = kwargs['instance']
    storage, path = instance.file.storage, instance.file.path
    storage.delete(path)
