from django.urls import path

from movies import views

app_name = 'movies'

urlpatterns = [
    path('', views.browse, name='movie_browse'),
    path('<str:name_of_genre>', views.browse_by_genre, name="browse_by_genre"),
    path('movie_details/<int:movie_id>', views.movie_details, name="movie_details"),
    path('search/', views.search_results, name="search_results"),
]