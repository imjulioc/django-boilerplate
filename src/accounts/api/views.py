from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.conf import settings
import jwt

from ..models import User
from ..utils import generate_access_token, generate_refresh_token

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
@ensure_csrf_cookie
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if (username) is None or (password is None):
        return Response({'error': 'Username or password is required.'}, status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.filter(username=username).first()
    if (user is None) or not user.check_password(password):
        return Response({'error': 'Username or password is wrong.'}, status=status.HTTP_404_NOT_FOUND)
    response = Response()

    acces_token = generate_access_token(user_profile._id)
    refresh_token = generate_refresh_token(user_profile._id)

    response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
    response.data = {
        'acces_token': acces_token
    }
    return response

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
@csrf_protect
def refresh_token(request):
    refresh_token = request.COOKIES.get('refresh_token')

    if refresh_token is None:
        raise exceptions.AuthenticationFailed(
            'Authorization credentials not provided.'
        )
    try:
        payload = jwt.decode(
            refresh_token, 
            settings.REFRESH_TOKEN_KEY, 
            algorithms=['HS256']
        )
    except jwt.ExpiredSignatureError:
        raise exceptions.AuthenticationFailed(
                'Expired access.'
            )

    user = User.objects.filter(_id=payload['_id']).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found.')
    if not user.is_active:
            raise exceptions.AuthenticationFailed('User is not active.')

    access_token = generate_access_token(user._id)

    return Response({'access_token': access_token})