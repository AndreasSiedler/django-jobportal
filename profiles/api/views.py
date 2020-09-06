from .serializers.common import CompanySerializer, CandidateSerializer
from ..models import Company, Candidate

from rest_framework import status, generics, permissions, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


# Company
class UserCompanyListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        """
        This view should return a list of all the companies
        for the currently authenticated user.
        """
        user = self.request.user
        return Company.objects.filter(user=user)


# Company
class CompanyListView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user',]


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