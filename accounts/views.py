from django.shortcuts import render
# from rest_framework import generics, status, views, permissions
from .serializers import RegisterSerializer
# from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
# from rest_framework.views import APIView
import jwt
# from django.conf import settings

from django.http import HttpResponsePermanentRedirect
import os
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

class CustomRedirect(HttpResponsePermanentRedirect):

    allowed_schemes = [os.environ.get('APP_SCHEME'), 'http', 'https']


class RegisterView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer



