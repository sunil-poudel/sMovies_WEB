from django.contrib import admin
from accounts.models import AppAssets, UserProfile

# Register your models here.
admin.site.register(AppAssets)
admin.site.register(UserProfile)