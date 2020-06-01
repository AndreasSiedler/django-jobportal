from django.db import models
from django.utils import timezone

from django.contrib.postgres.fields import JSONField, ArrayField
from django.core.exceptions import ValidationError

from accounts.models import User
from profiles.models import Company

# JOB_TYPE = (
#     ('1', "Full time"),
#     ('2', "Part time"),
#     ('3', "Internship"),
# )


SKILL_LEVEL = (
    ('1', "Beginner"),
    ('2', "Advanced"),
    ('3', "Expert"),
)

TYPE_LEVEL = (
    ('1', "Junior"),
    ('2', "Advanced"),
    ('3', "Senior"),
)

# Categories
class Category(models.Model):
    title    = models.CharField(max_length=150)
    slug     = models.SlugField(max_length = 250)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

# Locations
class Location(models.Model):
    title    = models.CharField(max_length=150)
    slug     = models.SlugField(max_length = 250, null = True, blank = True)

    def __str__(self):
        return self.title

# Tasks
class Task(models.Model):
    title    = models.CharField(max_length=150)
    slug     = models.SlugField(max_length = 250, null = True, blank = True)

    def __str__(self):
        return self.title

# Offers
class Offer(models.Model):
    title    = models.CharField(max_length=150)

    def __str__(self):
        return self.title

# Softskills
class Softskill(models.Model):
    title    = models.CharField(max_length=300)

    def __str__(self):
        return self.title  

# Hardskills
class Hardskill(models.Model):
    title           = models.CharField(max_length=300)
    dependency      = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    needs           = JSONField()

    def save(self, *args, **kwargs):
        # if self.dependency:
        #     print(self.dependency.id)
        if self.dependency and self.dependency.id == self.id:
            raise ValidationError('You can\'t have yourself as a dependency!')
        return super(Hardskill, self).save(*args, **kwargs)

    def __str__(self):
        return self.title  


# Types
class Type(models.Model):
    title               = models.CharField(max_length=150)
    slug                = models.SlugField(max_length=250, unique=True)
    level               = models.CharField(choices=TYPE_LEVEL, max_length=10, null=True)
    description         = models.TextField()
    category            = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    offers              = models.ManyToManyField(to='jobs.Offer')
    tasks               = models.ManyToManyField(to='jobs.Task')
    hardskills          = models.ManyToManyField(to='jobs.Hardskill', through='TypeHardSkill')
    softskills          = models.ManyToManyField(to='jobs.Softskill', through='TypeSoftSkill')
    created_at          = models.DateTimeField(default=timezone.now)

    def __str__(self):
        index_skill_level   = int(self.level) - 1
        skill_level         = TYPE_LEVEL[index_skill_level][1]
        return f"{self.title} ({skill_level})"


class TypeHardSkill(models.Model):
    type        = models.ForeignKey(Type, on_delete=models.CASCADE)
    skill       = models.ForeignKey(Hardskill, on_delete=models.CASCADE)
    level       = models.CharField(choices=SKILL_LEVEL, max_length=10)

    class Meta:
        unique_together     = (('type', 'skill'),)
        index_together      = (('type', 'skill'),)

class TypeSoftSkill(models.Model):
    type        = models.ForeignKey(Type, on_delete=models.CASCADE)
    skill       = models.ForeignKey(Softskill, on_delete=models.CASCADE)
    level       = models.CharField(choices=SKILL_LEVEL, max_length=10)

    class Meta:
        unique_together = (('type', 'skill'),)
        index_together = (('type', 'skill'),)


# Jobs
class Job(models.Model):
    company             = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    description         = models.TextField()
    type                = models.ForeignKey(Type, on_delete=models.CASCADE)
    location            = models.ForeignKey(Location, on_delete=models.CASCADE)
    offers              = models.ManyToManyField(to='jobs.Offer')
    tasks               = models.ManyToManyField(to='jobs.Task')
    hardskills          = models.ManyToManyField(to='jobs.Hardskill', through='JobHardSkill')
    softskills          = models.ManyToManyField(to='jobs.Softskill', through='JobSoftSkill')
    active              = models.BooleanField(default=True)
    created_by          = models.ForeignKey(User, related_name="jobs", on_delete=models.CASCADE)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)

    def save(self, request, *args, **kwargs):
        if self.user is None:
            self.user = request.user
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.type} ({self.company})"


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


# Applicants
class Applicant(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    job             = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applicants')
    created_at      = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = (('user', 'job'),)
        index_together = (('user', 'job'),)

    def __str__(self):
        return self.user