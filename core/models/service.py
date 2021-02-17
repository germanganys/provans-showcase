from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse


class ServiceCategory(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    price = models.CharField(max_length=16)
    image = models.ImageField()
    sort_priority = models.IntegerField()

    class Meta:
        ordering = ["sort_priority"]

    TYPE_CHOICES = (
        ('_hair', 'Волосы'),
        ('_nails', 'Ногти'),
    )
    service_type = models.CharField(max_length=128, choices=TYPE_CHOICES, default='_hair')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service_details_page', kwargs={'service_id': self.id})


@receiver(post_delete, sender=Service)
def service_image_delete_handler(sender, **kwargs):
    listing_image = kwargs['instance']
    storage, path = listing_image.image.storage, listing_image.image.path
    storage.delete(path)
