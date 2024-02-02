import datetime

import jwt
from django.contrib.auth.models import User
from rest_framework import serializers

from ecommerce_project.settings import JWT_SECRET_KEY


class JWTSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128,write_only=True)
    token = serializers.CharField(max_length=255,read_only=True)

    def create(self,validate_data):
        username = validate_data['user_name']
        password = validate_data['password']
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            payload = {
                'user_id': user.id,
                'exp': datetime.utcnow() + datetime.timedelta(JWT_SECRET_KEY),
            }
            token = jwt.encode(payload,JWT_SECRET_KEY, algorithm='HS256')
            return {"username" : username,"token" : token}
        else:
            return serializers.ValidationError('Invalid Username and password')
    def update(self,instance,validated_data):
        raise NotImplementedError('Method not implemented.')