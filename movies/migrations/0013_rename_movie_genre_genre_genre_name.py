# Generated by Django 5.1.3 on 2024-11-29 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0012_genre_about_genre"),
    ]

    operations = [
        migrations.RenameField(
            model_name="genre",
            old_name="movie_genre",
            new_name="genre_name",
        ),
    ]
