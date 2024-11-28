from django.shortcuts import render, redirect

from movies.models import Genre


# Create your views here.
def browse(request):
    genres = Genre.objects.all()
    context = {'genres':genres}
    return render(request, 'browse_movies.html', context)
