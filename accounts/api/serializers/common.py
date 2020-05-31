from rest_framework import serializers
from ...models import User
from django.utils.translation import ugettext_lazy as _

from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email


class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model=User
    fields = ('id', 'email', 'first_name', 'last_name',)


class RegisterSerializer(serializers.Serializer):
    """
    https://stackoverflow.com/questions/36910373/django-rest-auth-allauth-registration-with-email-first-and-last-name-and-witho
    """
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True) # Doesnt has password2 field in User Model
    is_employer = serializers.BooleanField(required=True, write_only=True)
    is_employee = serializers.BooleanField(required=True, write_only=True)


    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                _("The two password fields didn't match."))
        return data

    def save(self, request):
        print(self.validated_data)
        user = User(
            email = self.validated_data['email'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            is_employer = self.validated_data['is_employer'],
            is_employee = self.validated_data['is_employee'],
        )
        user.set_password(self.validated_data['password1'])
        user.save()
        return user