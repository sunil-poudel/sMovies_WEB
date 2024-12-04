
from django.db import models

# Create your models here.
class Movies(models.Model):
    LANGUAGE_CHOICES = [
        ('EN', 'English'),
        ('NP', 'Nepali'),
        ('ES', "Spanish"),
        ('HI', 'Hindi'),
        ('KO', 'Korean'),
        ('JP', 'Japanese'),
        ('CH', 'Chinese')
    ]
    name = models.TextField()
    release_date = models.DateField(null=True, blank=True)
    short_theme = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, blank=True, null=True)
    genre_name = models.ForeignKey('Genre', on_delete=models.CASCADE, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    movie_poster = models.ImageField(upload_to='movie_posters', blank=True, null=True)
    movie_poster_link = models.TextField(blank=True, null=True)
    trailer_embed_link = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    gpt_review = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name


class Genre(models.Model):
    genre_name = models.TextField()
    about_genre = models.TextField(null=True, blank=True)
    genre_poster = models.ImageField(upload_to='genre_posters', blank=True, null=True)

    def __str__(self):
        return self.genre_name