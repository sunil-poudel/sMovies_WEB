from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

from accounts.forms import AppAssetsForm, UserProfileForm


# Test function to check if the user is an admin
def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def app_assets(request):
    if request.method=='POST':
        form = AppAssetsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AppAssetsForm()

    context={'form':form}
    return render(request, 'app_assets.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return render(request, 'home.html')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, "registration/register.html", context)

def update_profile(request):
    if request.method=='POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserProfileForm(instance=request.user.user_profile)
    context = {'form':form}
    return render(request, 'update_profile.html', context)

