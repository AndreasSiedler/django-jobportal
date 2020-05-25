from django.urls import path
from accounts.api.views import (UserListView, UserView,)

urlpatterns = [
    path("users/", UserListView.as_view(), name="user-list"),
    path("users/<int:pk>/", UserView.as_view(), name="user-detail"),
]