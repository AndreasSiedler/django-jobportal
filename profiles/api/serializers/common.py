from rest_framework import serializers
from ...models import *
from accounts.api.serializers.nested import UserSerializer
from jobs.api.serializers.nested import TaskSerializer

# Company
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("id", "user", "title", "description", "website",)

    def to_representation(self, instance):
        self.fields['user'] =  UserSerializer(read_only=True)
        return super(CompanySerializer, self).to_representation(instance)

# Candidate
class CandidateHardskillSerializer(serializers.ModelSerializer):
    """Used as a nested serializer by CandidateSerializer"""
    skill       = serializers.StringRelatedField()
    # level       = serializers.StringRelatedField()

    class Meta:
        model   = CandidateHardSkill
        fields  = ("id", "skill", "level",)


class CandidateSerializer(serializers.ModelSerializer):
    
    # Related fields
    # tasks       = serializers.StringRelatedField(many=True)
    tasks       = TaskSerializer(many=True)
    hardskills  = serializers.SerializerMethodField()

    class Meta:
        model   = Candidate
        fields  = ("id", "user", "tasks", "jobtype", "hardskills",)

    
    def get_hardskills(self, obj):
        "obj is a candidate instance. Returns list of dicts"""
        qset = CandidateHardSkill.objects.filter(candidate=obj)
        return [CandidateHardskillSerializer(m).data for m in qset]

    def to_representation(self, instance):
        self.fields['user'] =  UserSerializer(read_only=True)
        return super(CandidateSerializer, self).to_representation(instance)