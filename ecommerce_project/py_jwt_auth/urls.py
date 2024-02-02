from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from py_jwt_auth import views

urlpatterns = [
    path('token/',views.ObtainTokenPairView.as_view(),name='get_new_token'),
    path('token/refresh/',views.RefreshTokenView.as_view(),name='refresh_token'),
    path('token/refresh/',views.VerifyTokenView.as_view(),name='verify_token'),
]