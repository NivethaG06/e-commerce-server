from django.urls import path

from userservice import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register/',views.refresh_token(),name='register'),
    # path('login/',views.refresh_token(),name='login'),
    path('profile/',views.refresh_token(),name='profile'),
    path('profile/update/',views.refresh_token(),name='profile_update'),
]