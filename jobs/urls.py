from django.urls import path, include, re_path

from .views import *

app_name = "jobs"

urlpatterns = [
    # Front
    path('', home_view, name='home'),
    path('search', SearchView.as_view(), name='search'),
    path('apply-job/<int:job_id>', ApplyJobView.as_view(), name='apply-job'),
    path('jobs', JobListView.as_view(), name='jobs'),
    path('jobs/<int:id>', JobDetailsView.as_view(), name='jobs-detail'),
    
    # Dash
    path('employer/dashboard/', include([
        path('', DashboardView.as_view(), name='employer-dashboard'),
        path('all-applicants', ApplicantsListView.as_view(), name='employer-all-applicants'),
        path('applicants/<int:job_id>', ApplicantPerJobView.as_view(), name='employer-dashboard-applicants'),
        path('mark-filled/<int:job_id>', filled, name='job-mark-filled'),
    ])),
    path('employer/jobs/create', JobCreateView.as_view(), name='employer-jobs-create'),
    path('employer/jobs/update/<int:id>', JobUpdateView.as_view(), name='employer-jobs-update'),
    path('employer/jobs/delete/<int:id>', JobDeleteView.as_view(), name='employer-jobs-delete'),
    # path('employer/skills/add/<int:id>', SkillAddView.as_view(), name='employer-skill-add'),
]
