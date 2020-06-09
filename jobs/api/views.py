# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from ..models import *
from .serializers.common import *
from rest_framework import generics
# Create your views here.


# Tasks
class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'category',]

# Types
class TypeListView(generics.ListAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    
# Jobs
class JobListView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()

