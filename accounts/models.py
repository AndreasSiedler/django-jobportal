# accounts.models.py

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager



class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    is_employee     = models.BooleanField(default=False)
    is_employer     = models.BooleanField(default=False)

    def __str__(self):
        return self.email