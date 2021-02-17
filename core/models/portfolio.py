from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete


class PortfolioPhoto(models.Model):
    image = models.ImageField()

    def __str__(self):
        return self.image.name


@receiver(post_delete, sender=PortfolioPhoto)
def promo_image_delete_handler(sender, **kwargs):
    instance = kwargs['instance']
    storage, path = instance.image.storage, instance.image.path
    storage.delete(path)
