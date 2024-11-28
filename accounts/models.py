from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class AppAssets(models.Model):
    logos = models.ImageField(upload_to='logos/', blank=True, null=True)
    movies_banner = models.ImageField(upload_to='banners/', blank=True, null=True)
    tickets_banner = models.ImageField(upload_to='banners/', blank=True, null=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_picture/", null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    try:
        instance.user_profile.save()
    except ObjectDoesNotExist:
        UserProfile.objects.create(user=instance)


