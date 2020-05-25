from django.urls import path
from profiles.api.views import CompanyListView, CompanyView

urlpatterns = [
    path("companies/", CompanyListView.as_view(), name="company-list"),
    path("companies/<int:pk>/", CompanyView.as_view(), name="company-detail"),
]