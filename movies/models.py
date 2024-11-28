
from django.db import models

# Create your models here.
class Movies(models.Model):
    LANGUAGE_CHOICES = [
        ('EN', 'English'),
        ('NP', 'Nepali'),
        ('ES', "Spanish"),
        ('HI', 'Hindi'),
        ('OT', 'Others')
    ]
    name = models.TextField()
    release_date = models.DateField(null=True, blank=True)
    short_theme = models.TextField()
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, blank=True, null=True)
    movie_genre = models.ForeignKey('Genre', on_delete=models.CASCADE, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    movie_genre = models.TextField()

    def __str__(self):
        return self.movie_genre