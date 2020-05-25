from rest_framework import serializers
from ..models import Company
from accounts.api.serializers import UserSerializer

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("id", "user", "title", "description", "website",)

    def to_representation(self, instance):
        self.fields['user'] =  UserSerializer(read_only=True)
        return super(CompanySerializer, self).to_representation(instance)