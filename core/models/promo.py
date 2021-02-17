from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django.db.models.signals import post_delete


class Promo(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=2048)
    image = models.ImageField(null=True)
    offer_info = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('promo_details_page', kwargs={'promo_id': self.id})


@receiver(post_delete, sender=Promo)
def promo_image_delete_handler(sender, **kwargs):
    if 'instance' in kwargs:
        instance = kwargs['instance']
        storage, path = instance.image.storage, instance.image.path
        storage.delete(path)


@receiver(post_delete, sender=Promo)
def promo_offer_info_delete_handler(sender, **kwargs):
    if 'instance' in kwargs:
        instance = kwargs['instance']
        storage, path = instance.offer_info.storage, instance.offer_info.path
        storage.delete(path)


class DiscountCoupon(models.Model):
    code = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now=True, editable=True)
    used = models.BooleanField(default=False)

    def __str__(self):
        return self.code + ' получен: ' + str(self.timestamp) + 'Использован' if self.used else ''

