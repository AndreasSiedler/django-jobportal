"""job_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from allauth.account.views import confirm_email
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include


from rest_auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path("api/rest-auth/", include("rest_auth.urls")),
    # path("api/rest-auth/registration/", include("rest_auth.registration.urls")),
    url(r'^api/v1/rest-auth/', include('rest_auth.urls')),
    url(r'^api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api/v1/account/', include('allauth.urls')),
    url(r'^api/v1/accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),

    path("api/v1/jobs/", include("jobs.api.urls")),
    path("api/v1/accounts/", include("accounts.api.urls")),
    path("api/v1/profiles/", include("profiles.api.urls")),

    path('', include('jobs.urls')),
]
