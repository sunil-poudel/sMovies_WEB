from django import forms

from movies.models import Movies, Genre


class MoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = {'name', 'release_date', 'short_theme', 'language'}
        labels = {
            'name':'name of movie',
            'release_date':'date of release',
            'short_theme':'theme of movie in short',
            'language':'language'
        }

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = {'movie_genre'}
        labels = {'movie_genre':'genre'}
