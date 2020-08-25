from django.urls import path

from .views import UserCreate, login, refresh_token

urlpatterns = [
    path('signup/', UserCreate.as_view(), name='signup'),
    path('login/', login, name='login'),
    path('refresh_token/', refresh_token, name='refresh_token'),
]