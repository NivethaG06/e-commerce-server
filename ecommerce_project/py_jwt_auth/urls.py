from django.urls import path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('token/',views.TokenObtainPairView.as_view(),name='get_token'),
    path('token/refresh/',views.TokenRefreshView.as_view(),name='refresh_token'),
]