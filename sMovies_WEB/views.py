from django.shortcuts import render

from accounts.models import AppAssets


def home(request):
    logo = AppAssets.objects.get(id=7)
    imdb = AppAssets.objects.get(id=9)
    rotten_tomatoes = AppAssets.objects.get(id=10)
    movies_banner = AppAssets.objects.get(id=11)
    context = {'logo':logo, 'imdb':imdb, 'rotten_tomatoes':rotten_tomatoes, 'movies_banner':movies_banner}
    return render(request, "home.html", context)

