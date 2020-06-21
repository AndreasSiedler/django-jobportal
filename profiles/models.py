import os
from django.db import models
from django.utils import timezone

SKILL_LEVEL = (
    ('1', "Beginner"),
    ('2', "Advanced"),
    ('3', "Expert"),
)


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

# Candidate
class Candidate(models.Model):
    user                = models.ForeignKey('accounts.User', on_delete=models.CASCADE, blank=True)
    tasks               = models.ManyToManyField('jobs.Task')
    jobtype             = models.ForeignKey('jobs.Type', on_delete=models.CASCADE)
    # experience          = models.ManyToManyField('jobs.Type', through='CandidateTypeExperience')
    hardskills          = models.ManyToManyField('jobs.Hardskill', through='CandidateHardSkill')
    softskills          = models.ManyToManyField('jobs.Softskill', through='CandidateSoftSkill')
    created_at          = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = (('user', 'jobtype'),)
        index_together = (('user', 'jobtype'),)

    def __str__(self):
        return f"{self.user.email} ({self.jobtype.title})" 

class CandidateHardSkill(models.Model):
    candidate       = models.ForeignKey('profiles.Candidate', on_delete=models.CASCADE, related_name='candidate_to_skill')
    skill           = models.ForeignKey('jobs.Hardskill', on_delete=models.CASCADE, related_name='skill_to_candidate')
    level           = models.CharField(choices=SKILL_LEVEL, max_length=10)

    class Meta:
        unique_together = (('candidate', 'skill'),)
        index_together = (('candidate', 'skill'),)

class CandidateSoftSkill(models.Model):
    candidate       = models.ForeignKey('profiles.Candidate', on_delete=models.CASCADE)
    skill           = models.ForeignKey('jobs.Softskill', on_delete=models.CASCADE)
    level           = models.CharField(choices=SKILL_LEVEL, max_length=10)

    class Meta:
        unique_together = (('candidate', 'skill'),)
        index_together = (('candidate', 'skill'),)


# Companies
class Company(models.Model):   
    user            = models.ForeignKey('accounts.User', related_name="companies", on_delete=models.CASCADE)
    title           = models.CharField(max_length=100)
    slug            = models.SlugField(max_length=100)
    logo            = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    description     = models.TextField()
    website         = models.CharField(max_length=100)
    created_by          = models.ForeignKey('accounts.User', on_delete=models.CASCADE, editable=False)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "companies"
    
    def __str__(self):
        return f"{self.title}"

# Locations
class Location(models.Model):   
    company         = models.ForeignKey('profiles.Company', on_delete=models.CASCADE)
    title           = models.CharField(max_length=100)
    longitude       = models.CharField(max_length=300)
    latitude        = models.CharField(max_length=300)
