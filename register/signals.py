from .models import Profile
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(post_save, sender=Profile)
def profileUpdated(sender, instance, created, **kwargs):
    print('profile saved!')

@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user    = instance
        profile = Profile.objects.create(
            user     = user,
            username = user.username,
            name     = user.first_name,
            email    = user.email,
        )

@receiver(post_delete, sender=Profile)
def deleteProfile(sender, instance, created, **kwargs):
    user = instance.user
    user.delete()



# post_save.connect(profileUpdated, sender=Profile)
