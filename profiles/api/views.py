from .serializers.common import CompanySerializer, CandidateSerializer
from ..models import Company, Candidate

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics


# Company
class CompanyListView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

# Candidate
class CandidateListView(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class CandidateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()


# @api_view(['POST'])
# def company_create(request):
#   serializer = CompanySerializer(data=request.data)
#   if serializer.is_valid():
#     serializer.save()
#     return Response(serializer.data, status = status.HTTP_201_CREATED)
#   return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)