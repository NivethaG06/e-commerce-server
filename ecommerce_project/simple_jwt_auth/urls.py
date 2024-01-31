from django.urls import path

urlpatterns = [
    path('simple/token/',views.TokenObtainPairView.as_view(),name='get_token'),
    path('simple/token/refresh/',views.TokenRefreshView.as_view(),name='refresh_token'),
]