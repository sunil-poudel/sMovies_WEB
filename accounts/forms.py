from django import forms
from accounts.models import AppAssets, UserProfile


class AppAssetsForm(forms.ModelForm):
    class Meta:
        model = AppAssets
        fields = '__all__'

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture' ]
        labels = {'bio':'enter your bio', 'profile_picture':'upload profile picture'}