from django.shortcuts import render, redirect

from movies.models import Genre, Movies


# Create your views here.
def browse(request):
    genres = Genre.objects.all()
    context = {'genres':genres}
    return render(request, 'browse_movies.html', context)

def browse_by_genre(request, name_of_genre):
    genre = Genre.objects.get(genre_name__iexact=name_of_genre)
    movies_by_genre = Movies.objects.filter(genre_name=genre.id)
    context = {'movies_by_genre':movies_by_genre}
    return render(request, 'movies_by_genre.html', context)

def movie_details(request, movie_id):
    movie = Movies.objects.get(id=movie_id)
    context={'movie':movie}
    return render(request, 'movie_details.html', context)

def search_results(request):
    query = request.GET.get('query')
    results = Movies.objects.filter(name__icontains=query)
    context = {'query':query, 'results':results}
    return render(request, 'search_results.html', context)