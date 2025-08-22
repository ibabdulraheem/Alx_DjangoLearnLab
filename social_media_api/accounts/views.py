from django.shortcuts import render
from rest_framework import generics,views
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer
from rest_framework import response

#Views for Registration endpoint
User = get_user_model()
class RegistrationView(generics.CreateApiView):
  queryset = User.objects.all()
  serializer_class = RegisterSerializer

#Login View that return 'Token'
class LoginView(ObtainAuthToken):
  def post(self, request, *args, **kwargs):
    return super().post(request, *args, **kwargs)
  token = Token.objects.get(key = response.data['Token'])
  Response({
    'token': token.key,
    'user_id': token.user_id,
    'username': token.user.username
  })




