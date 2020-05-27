from rest_framework import serializers
from ...models import Company, Candidate, CandidateHardSkill
from accounts.api.serializers.nested import UserSerializer
from jobs.api.serializers.nested import TaskSerializer
from jobs.models import Hardskill, Task

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
    # skill       = serializers.StringRelatedField()
    # level       = serializers.StringRelatedField()

    class Meta:
        model   = CandidateHardSkill
        fields  = ("id", "skill", "level")


class CandidateSerializer(serializers.ModelSerializer):
    
    hardskills  = CandidateHardskillSerializer(source='candidate_to_skill', many=True)

    class Meta:
        model   = Candidate
        fields  = ("id", "user", "tasks", "jobtype", "hardskills",)
    
    # def get_hardskills(self, obj):
    #     "obj is a candidate instance. Returns list of dicts"""
    #     qset = CandidateHardSkill.objects.filter(candidate=obj)
    #     return [CandidateHardskillSerializer(m).data for m in qset]

    def create(self, validated_data):
        tasks               = validated_data.pop('tasks')
        candidate_to_skill  = validated_data.pop('candidate_to_skill')
        candidate           = Candidate(**validated_data)
        candidate.save()
        candidate.tasks.set(tasks)

        for each in candidate_to_skill:
            each['candidate'] = candidate
            candidate_hardskill = CandidateHardSkill()
            candidate_hardskill.candidate = each["candidate"]
            candidate_hardskill.skill = each["skill"]
            candidate_hardskill.level = each["level"]   
            candidate_hardskill.save()

            # NOR WORKING:
            # CandidateHardSkill(**each)
            # CandidateHardSkill.save()
            # NOR WORKING:
            # CandidateHardSkill.objects.create(candidate=candidate, skill=candidate_to_skill, level="1")

        return candidate

    def update(self, instance, validated_data):
        print(validated_data)
        # Set Tasks
        tasks_data = validated_data.pop('tasks')
        instance.tasks.set(tasks_data)

        instance.user = validated_data.get('user', instance.user)
        instance.jobtype = validated_data.get('jobtype', instance.jobtype)
        instance.save()


        return instance


    # To just use serializer for GET
    def to_representation(self, instance):
        self.fields['user']     =  UserSerializer(read_only=True)
        self.fields['tasks']    =  TaskSerializer(many=True, read_only=True)
        return super(CandidateSerializer, self).to_representation(instance)