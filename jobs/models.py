from django.db import models
from django.utils import timezone

# from django.contrib.postgres.fields import JSONField, ArrayField

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

PROFILE_LEVEL = (
    ('1', "Junior"),
    ('2', "Advanced"),
    ('3', "Senior"),
)

# class Title(models.Model):
#     title    = models.CharField(max_length=150)
#     slug     = models.SlugField(max_length = 250, null = True, blank = True)

#     def __str__(self):
#         return self.title


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

class Task(models.Model):
    title    = models.CharField(max_length=150)
    slug     = models.SlugField(max_length = 250, null = True, blank = True)

    def __str__(self):
        return self.title

class Offer(models.Model):
    title    = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Softskill(models.Model):
    name    = models.CharField(max_length=300)
    type    = models.CharField(choices=SKILL_TYPE, max_length=10)

    def __str__(self):
        return self.name  


class Hardskill(models.Model):
    title    = models.CharField(max_length=300)

    def __str__(self):
        return self.title  


# Job Profiles
class Profile(models.Model):
    title               = models.CharField(max_length=150)
    slug                = models.SlugField(max_length = 250, blank = True)
    level               = models.CharField(choices=PROFILE_LEVEL, max_length=10, null = True)
    description         = models.TextField()
    category            = models.ForeignKey(Category, on_delete=models.CASCADE, null = True)
    offers              = models.ManyToManyField(to='jobs.Offer')
    tasks               = models.ManyToManyField(to='jobs.Task')
    hardskills          = models.ManyToManyField(to='jobs.Hardskill', through='ProfileHardSkill')
    softskills          = models.ManyToManyField(to='jobs.Softskill', through='ProfileSoftSkill')
    created_at          = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title + ' ' + self.level


class ProfileHardSkill(models.Model):
    profile     = models.ForeignKey(Profile, on_delete=models.CASCADE)
    skill       = models.ForeignKey(Hardskill, on_delete=models.CASCADE)
    level       = models.CharField(choices=SKILL_LEVEL, max_length=10)

    class Meta:
        unique_together = (('profile', 'skill'),)
        index_together = (('profile', 'skill'),)

class ProfileSoftSkill(models.Model):
    profile     = models.ForeignKey(Profile, on_delete=models.CASCADE)
    skill       = models.ForeignKey(Softskill, on_delete=models.CASCADE)
    level       = models.CharField(choices=SKILL_LEVEL, max_length=10)

    class Meta:
        unique_together = (('profile', 'skill'),)
        index_together = (('profile', 'skill'),)


# Jobs
class Job(models.Model):
    company             = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    profile             = models.ForeignKey(Profile, on_delete=models.CASCADE)
    location            = models.ForeignKey(Location, on_delete=models.CASCADE)
    offers              = models.ManyToManyField(to='jobs.Offer')
    tasks               = models.ManyToManyField(to='jobs.Task')
    hardskills          = models.ManyToManyField(to='jobs.Hardskill', through='JobHardSkill')
    softskills          = models.ManyToManyField(to='jobs.Softskill', through='JobSoftSkill')
    created_at          = models.DateTimeField(default=timezone.now)
    created_by          = models.ForeignKey(User, on_delete=models.CASCADE)



class JobHardSkill(models.Model):
    job         = models.ForeignKey(Job, on_delete=models.CASCADE)
    skill       = models.ForeignKey(Hardskill, on_delete=models.CASCADE)
    level       = models.CharField(choices=SKILL_LEVEL, max_length=10)

    class Meta:
        unique_together = (('job', 'skill'),)
        index_together = (('job', 'skill'),)

class JobSoftSkill(models.Model):
    job         = models.ForeignKey(Job, on_delete=models.CASCADE)
    skill       = models.ForeignKey(Softskill, on_delete=models.CASCADE)
    level       = models.CharField(choices=SKILL_LEVEL, max_length=10)

    class Meta:
        unique_together = (('job', 'skill'),)
        index_together = (('job', 'skill'),)


# Applicant
class Applicant(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    job             = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applicants')
    created_at      = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = (('user', 'job'),)
        index_together = (('user', 'job'),)

    def __str__(self):
        return self.user