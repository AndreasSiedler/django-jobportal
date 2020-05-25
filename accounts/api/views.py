# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from ..models import *
from .serializers import *
from rest_framework import generics
# Create your views here.


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()