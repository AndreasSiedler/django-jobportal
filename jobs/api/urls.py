from django.urls import path
from jobs.api.views import JobListView, TaskListView, JobView, TypeListView

urlpatterns = [
    # Jobs
    path("jobs/", JobListView.as_view(), name="job-list"),
    path("jobs/<int:pk>/", JobView.as_view(), name="job-detail"),
    # Types
    path("types/", TypeListView.as_view(), name="type-list"),
    # Tasks
    path("tasks/", TaskListView.as_view(), name="task-list"),
    # path("types/<int:pk>/", JobView.as_view(), name="type-detail"),
]