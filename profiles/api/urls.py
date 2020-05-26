from django.urls import path
from profiles.api.views import *

urlpatterns = [
    # Company
    path("companies/", CompanyListView.as_view(), name="company-list"),
    path("companies/<int:pk>/", CompanyView.as_view(), name="company-detail"),
    # Candidate
    path("candidates/", CandidateListView.as_view(), name="candidate-list"),
    path("candidates/<int:pk>/", CandidateView.as_view(), name="candidate-detail"),
]