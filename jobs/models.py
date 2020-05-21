from django.db import models
from django.utils import timezone

from django.contrib.postgres.fields import JSONField, ArrayField

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

SKILL_LEVEL = (
    ('1', "Beginner"),
    ('2', "Advanced"),
    ('3', "Expert"),

)


class Title(models.Model):
    title    = models.CharField(max_length=150)
    slug     = models.SlugField(max_length = 250, null = True, blank = True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title    = models.CharField(max_length=150)
    slug     = models.SlugField(max_length = 250)

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
    title               = models.ForeignKey(Title, on_delete=models.CASCADE)
    description         = models.TextField()
    location            = models.ForeignKey(Location, on_delete=models.CASCADE)
    tasks               = ArrayField(models.CharField(max_length=300), null=True)
    offers              = ArrayField(models.CharField(max_length=300), null=True)
    skills              = models.ManyToManyField(Skill, through='Skillship')
    created_at          = models.DateTimeField(default=timezone.now)
    company             = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    # skills              = JSONField()
    # type                = models.CharField(choices=JOB_TYPE, max_length=10)
    # category            = models.ForeignKey(Category, on_delete=models.CASCADE)
    # salary              = RangeField()
    # company             = models.ForeignKey(Company, on_delete=models.CASCADE)
    # filled              = models.BooleanField(default=False)
    # company_name        = models.CharField(max_length=100)
    # company_description = models.CharField(max_length=300)
    # website             = models.CharField(max_length=100, default="")



class Skillship(models.Model):
    job     = models.ForeignKey(Job, on_delete=models.CASCADE)
    skill   = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level   = models.CharField(choices=SKILL_LEVEL, max_length=10)

    class Meta:
        unique_together = (('job', 'skill'),)
        index_together = (('job', 'skill'),)


class Applicant(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    job             = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applicants')
    created_at      = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = (('user', 'job'),)
        index_together = (('user', 'job'),)

    def __str__(self):
        return self.user