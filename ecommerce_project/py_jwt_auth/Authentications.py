from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication
import jwt
from rest_framework.exceptions import AuthenticationFailed

from ecommerce_project.settings import JWT_SECRET_KEY


class PY_JWT_AUTHENTICATION(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('Authorization','').split(' ')[1]
        try:
            payload = jwt.decode(token,JWT_SECRET_KEY,algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            return (user,None)
        except User.DoesNotExist:
            raise AuthenticationFailed('User Failed')
        except jwt.DecodeError:
            raise AuthenticationFailed('Invalid Valid')