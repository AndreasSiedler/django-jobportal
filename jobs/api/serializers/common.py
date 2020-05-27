from rest_framework import (serializers, filters)
from ...models import *
from profiles.api.serializers.nested import CompanySerializer

# Type
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Type
        fields  = ("id", "title",)

# Hardskill
class HardskillSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Hardskill
        fields  = ("title",)

# Job
class JobSerializer(serializers.ModelSerializer):

    company = CompanySerializer(read_only=True)
    # profile = serializers.StringRelatedField()
    # location = serializers.StringRelatedField()
    
    class Meta:
        model   = Job
        fields  = ("company", )
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
