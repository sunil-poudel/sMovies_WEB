from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AppAssets(models.Model):
    logos = models.ImageField(upload_to='logos/', blank=True, null=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    intro = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add = True)
    profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True, null=True)

    def __str__(self):
        return self.user.username



