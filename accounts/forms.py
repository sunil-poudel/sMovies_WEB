from django import forms
from accounts.models import UserProfile, AppAssets

class AppAssetsForm(forms.ModelForm):
    class Meta:
        model = AppAssets
        fields = '__all__'

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

