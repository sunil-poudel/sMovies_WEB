# Generated by Django 5.1.3 on 2024-11-29 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0011_movies_gpt_review_movies_summary"),
    ]

    operations = [
        migrations.AddField(
            model_name="genre",
            name="about_genre",
            field=models.TextField(blank=True, null=True),
        ),
    ]