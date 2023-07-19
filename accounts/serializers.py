from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from accounts.models import BaseUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(trim_whitespace=False, write_only=True)

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = BaseUser.objects.create_user(**validated_data)
        return user

    class Meta:
        model = BaseUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
