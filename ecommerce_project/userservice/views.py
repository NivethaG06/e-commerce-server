from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from userservice import CustomUser


# Create your views here.
# class ObtainTokenPairView(APIView):
#     permission_classes = [AllowAny]
#
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         if not username or not password:
#             return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)
#
#         user = get_user_model().objects.filter(username=username).first()
#         if not user or not user.check_password(password):
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#
#         refresh = RefreshToken.for_user(user)
#         return Response({
#             'access': str(refresh.access_token),
#             'refresh': str(refresh),
#         })
#         # return Response({"message": "Success."})
#
# @api_view(['GET'])
# @permission_classes(['IsAuthenticated'])
# def get_new_token():
#     return Response({"message" : "This is a protected view."})
#
# def refresh_token():
#     return

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
