# Generated by Django 5.1.3 on 2024-11-28 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0008_genre_genre_poster_movies_movie_poster"),
    ]

    operations = [
        migrations.AddField(
            model_name="movies",
            name="movie_poster_link",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="movies",
            name="trailer_embed_link",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="movies",
            name="short_theme",
            field=models.TextField(blank=True, null=True),
        ),
    ]
