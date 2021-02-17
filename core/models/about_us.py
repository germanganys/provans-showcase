from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.urls import reverse


class About(models.Model):
    name = models.CharField(max_length=256, default='')
    description = models.TextField(max_length=2048, default='')
    image = models.ImageField(null=True)
    sort_priority = models.IntegerField(default=0)

    class Meta:
        ordering = ["sort_priority"]
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('about_details_page', kwargs={'about_id': self.id})


@receiver(post_delete, sender=About)
def promo_image_delete_handler(sender, **kwargs):
    instance = kwargs['instance']
    storage, path = instance.image.storage, instance.image.path
    storage.delete(path)
