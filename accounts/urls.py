from django.urls import include, path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', include('django.contrib.auth.urls')),
    path('app_assets/', views.app_assets, name='app_assets'),
    path('update_profile/', views.update_profile, name="update_profile"),
]