# Generated by Django 5.1.3 on 2024-11-28 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0007_alter_movies_language"),
    ]

    operations = [
        migrations.AddField(
            model_name="genre",
            name="genre_poster",
            field=models.ImageField(blank=True, null=True, upload_to="genre_posters"),
        ),
        migrations.AddField(
            model_name="movies",
            name="movie_poster",
            field=models.ImageField(blank=True, null=True, upload_to="movie_posters"),
        ),
    ]