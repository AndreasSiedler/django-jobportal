from rest_framework import serializers
from ..models import Job, Softskill, Applicant


class JobSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Job
        fields = ['id', 'title',]


class SoftskillSerializer(serializers.ModelSerializer):

    jobs = JobSerializer(many=True, read_only=True)

    class Meta:
        model = Softskill
        fields = ['id', 'name', 'jobs']


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = "__all__"
