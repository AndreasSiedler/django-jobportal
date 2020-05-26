from rest_framework import serializers
from ...models import *
from accounts.api.serializers.nested import UserSerializer

# Company
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("id", "user", "title", "description", "website",)

    def to_representation(self, instance):
        self.fields['user'] =  UserSerializer(read_only=True)
        return super(CompanySerializer, self).to_representation(instance)

