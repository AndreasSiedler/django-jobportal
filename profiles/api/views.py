from .serializers import CompanySerializer
from ..models import Company

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

class CompanyListView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


# @api_view(['POST'])
# def company_create(request):
#   serializer = CompanySerializer(data=request.data)
#   if serializer.is_valid():
#     serializer.save()
#     return Response(serializer.data, status = status.HTTP_201_CREATED)
#   return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)