from django.shortcuts import render

from accounts.models import AppAssets


def home(request):
    logo = AppAssets.objects.get(id=7)
    context = {'logo':logo}
    return render(request, "home.html", context)

def base(request):
    logo = AppAssets.objects.get(id=7)
    context = {'logo':logo}
    return render(request, "base.html", context)
