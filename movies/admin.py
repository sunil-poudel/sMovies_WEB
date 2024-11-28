from django.contrib import admin

from movies.models import Genre, Movies

# Register your models here.
admin.site.register(Genre)
admin.site.register(Movies)
