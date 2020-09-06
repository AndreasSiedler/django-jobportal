from rest_framework import (serializers, filters)
from ...models import *
from profiles.api.serializers.nested import CompanySerializer

# Education
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Education
        fields  = ("id", "title",)


# Task
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Task
        fields  = ("id", "title",)

# Offer
class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Offer
        fields  = ("id", "title",)

# Experience
# class ExperienceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model   = Experience
#         fields  = ("id", "title",)

class TypeExperienceSerializer(serializers.ModelSerializer):
    type_title = serializers.ReadOnlyField(source='from_type.title')
    type_id = serializers.ReadOnlyField(source='from_type.id')
    experience = serializers.ReadOnlyField(source='experience.title')
    experience_id = serializers.ReadOnlyField(source='experience.id')
    class Meta:
        model   = TypeExperience
        fields  = ('id', 'type_title', 'type_id', 'experience', 'experience_id',)

# Type
class TypeSerializer(serializers.ModelSerializer):

    offers = OfferSerializer(many=True)
    tasks = TaskSerializer(many=True)
    # experience = TypeExperienceSerializer(source='type_experience', many=True)
    experience = TypeExperienceSerializer(source='to_type', many=True)
    # experience = serializers.SerializerMethodField()
    education = EducationSerializer()
    class Meta:
        model   = Type
        fields  = ('id', 'title', 'description', 'tasks', 'offers', 'salarymin', 'salarymax', 'education', 'experience', 'hardskills', 'softskills', 'language', )
        read_only_fields = ('created_at','updated_at')
        # depth = 2

    # def get_experience(self, obj):
    #     print(obj)
    #     "obj is a Member instance. Returns list of dicts"""
    #     qset = TypeExperience.objects.filter(to_type=obj)
    #     return [TypeExperienceSerializer(m).data for m in qset]


# Hardskill
class HardskillSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Hardskill
        fields  = ("title",)

# Job
class JobSerializer(serializers.ModelSerializer):

    # company = CompanySerializer()
    # profile = serializers.StringRelatedField()
    # location = serializers.StringRelatedField()
    
    class Meta:
        model   = Job
        fields  = ('id', 'active', 'type', 'description', 'tasks', 'offers', 'salarymin', 'salarymax', 'education', 'company', 'location',)
        read_only_fields = ('created_at','updated_at')


    # def create(self, validated_data):
    #     job = Job.objects.create(**validated_data)
    #     return job

    # def update(self, instance, validated_data):
    #     albums_data = validated_data.pop('album_musician')
    #     albums = (instance.album_musician).all()
    #     albums = list(albums)
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.instrument = validated_data.get('instrument', instance.instrument)
    #     instance.save()

    #     for album_data in albums_data:
    #         album = albums.pop(0)
    #         album.name = album_data.get('name', album.name)
    #         album.release_date = album_data.get('release_date', album.release_date)
    #         album.num_stars = album_data.get('num_stars', album.num_stars)
    #         album.save()
    #     return instance


class SoftskillSerializer(serializers.ModelSerializer):

    jobs = JobSerializer(many=True, read_only=True)

    class Meta:
        model = Softskill
        fields = ['id', 'name', 'jobs']


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = "__all__"
