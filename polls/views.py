from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets

from polls.models import Users
from polls.serializers import Usersserializer


class UserView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = Usersserializer