from django.urls import path, include, re_path

from .views import *

app_name = "jobs"

urlpatterns = [
    path('', home_view, name='home'),
    path('search', SearchView.as_view(), name='search'),
    path('jobs', JobListView.as_view(), name='jobs'),
    path('jobs/<int:id>', JobDetailsView.as_view(), name='jobs-detail'),
]
