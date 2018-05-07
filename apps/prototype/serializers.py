from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Ship

User = get_user_model()

class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ship
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "pk", "password", "username")
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        errors = {}
        email = data.get("email", None)
        if email is None:
            errors['email'] = 'Email cannot be empty'
            raise serializers.ValidationError(errors)
        return data