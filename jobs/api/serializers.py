from rest_framework import serializers
from ..models import Job, Skill, Applicant


class JobSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Job
        fields = ['id', 'title',]


class SkillSerializer(serializers.ModelSerializer):

    jobs = JobSerializer(many=True, read_only=True)

    class Meta:
        model = Skill
        fields = ['id', 'name', 'jobs']


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = "__all__"
