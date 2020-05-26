from django.urls import path
from jobs.api.views import (JobListView, JobView,)

urlpatterns = [
    # Jobs
    path("jobs/", JobListView.as_view(), name="job-list"),
    path("jobs/<int:pk>/", JobView.as_view(), name="job-detail"),
]