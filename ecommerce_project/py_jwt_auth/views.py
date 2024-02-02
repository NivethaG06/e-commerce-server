import secrets

from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from py_jwt_auth.Authentications import PY_JWT_AUTHENTICATION
from py_jwt_auth.serializers import JWTSerializer



class ObtainTokenPairView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer = JWTSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)

class RefreshTokenView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        if not refresh_token:
            return Response({'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)
        new_tokens = secrets.token_urlsafe(16)
        return Response(new_tokens)

class VerifyTokenView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        authenticator = PY_JWT_AUTHENTICATION()
        authenticator.authenticate(request)
        return Response({'error': 'Token Verified'}, status=status.HTTP_200_OK)