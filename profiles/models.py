import os

from django.db import models
from django.utils import timezone

from accounts.models import User

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    # print(instance)
    # print(filename)
    new_filename = instance.slug
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "logos/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )

# Create your models here.
class Candidate(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at      = models.DateTimeField(default=timezone.now)


class Company(models.Model):   
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    title           = models.CharField(max_length=100)
    slug            = models.SlugField(max_length=100)
    logo            = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    description     = models.CharField(max_length=300)
    website         = models.CharField(max_length=100, default="")
    created_at      = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title