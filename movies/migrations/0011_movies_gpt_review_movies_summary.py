# Generated by Django 5.1.3 on 2024-11-29 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0010_alter_movies_language"),
    ]

    operations = [
        migrations.AddField(
            model_name="movies",
            name="gpt_review",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="movies",
            name="summary",
            field=models.TextField(blank=True, null=True),
        ),
    ]
