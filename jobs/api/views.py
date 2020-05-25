# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from ..models import *
from .serializers import *
from rest_framework import generics
# Create your views here.


class JobListView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()