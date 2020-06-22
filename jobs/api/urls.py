from django.urls import path
from jobs.api.views import JobListView, TaskListView, JobView, TypeListView, TypeView, EducationListView

urlpatterns = [
    # Jobs
    path("jobs/", JobListView.as_view(), name="job-list"),
    path("jobs/<int:pk>/", JobView.as_view(), name="job-detail"),
    # Types
    path("types/", TypeListView.as_view(), name="type-list"),
    path("types/<int:pk>/", TypeView.as_view(), name="type-detail"),
    # Tasks
    path("tasks/", TaskListView.as_view(), name="task-list"),
    # Education
    path("education/", EducationListView.as_view(), name="education-list"),
]