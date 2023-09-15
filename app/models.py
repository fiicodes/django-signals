from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Profile(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.name)


@receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    print('Profile created')


@receiver(post_delete, sender=Profile)
def deleteUProfile(sender, instance, **kwargs):
    print('Instance:', instance)
    print('Profile deleted')
