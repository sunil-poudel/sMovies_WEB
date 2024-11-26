from django.shortcuts import render

from accounts.models import AppAssets


def home(request):
    logo = AppAssets.objects.get(id=7)
    imdb = AppAssets.objects.get(id=9)
    rotten_tomatoes = AppAssets.objects.get(id=10)
    context = {'logo':logo, 'imdb':imdb, 'rotten_tomatoes':rotten_tomatoes}
    return render(request, "home.html", context)

