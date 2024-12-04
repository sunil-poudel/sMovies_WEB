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
        fields = {'genre_name'}
        labels = {'genre_name': 'genre'}

class SearchForm(forms.Form):
    query = forms.CharField(required=False, label='', widget=forms.TextInput(
        attrs={
            'placeholder':'search movies',
            'class':'form-control mr-sm-2',
        }
    ))
