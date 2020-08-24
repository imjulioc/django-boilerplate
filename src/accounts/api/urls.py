from django.urls import path

from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('refresh_token/', login, name='refresh_token'),
]