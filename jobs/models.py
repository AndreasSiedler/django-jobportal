from django.db import models
from django.utils import timezone

from accounts.models import User
from profiles.models import Company

JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)

SKILL_TYPE = (
    ('1', "Soft Skill"),
    ('2', "Technical Skill"),
)



class Category(models.Model):
    title    = models.CharField(max_length=150)
    slug     = models.SlugField(max_length = 250)

    def __str__(self):
        return self.title


class Type(models.Model):
    title    = models.CharField(max_length=300)

    def __str__(self):
        return self.title  
        

class Location(models.Model):
    title    = models.CharField(max_length=150)
    slug     = models.SlugField(max_length = 250, null = True, blank = True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    name    = models.CharField(max_length=300)
    type    = models.CharField(choices=SKILL_TYPE, max_length=10)

    def __str__(self):
        return self.name  


class Job(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    title               = models.CharField(max_length=300)
    description         = models.TextField()
    location            = models.CharField(max_length=150)
    type                = models.CharField(choices=JOB_TYPE, max_length=10)
    category            = models.CharField(max_length=100)
    last_date           = models.DateTimeField()
    company             = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    company_name        = models.CharField(max_length=100)
    company_description = models.CharField(max_length=300)
    website             = models.CharField(max_length=100, default="")
    created_at          = models.DateTimeField(default=timezone.now)
    filled              = models.BooleanField(default=False)
    salary              = models.IntegerField(default=0, blank=True)
    skills              = models.ManyToManyField(Skill, blank=True)


    def __str__(self):
        return self.title


class Applicant(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    job             = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applicants')
    created_at      = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user