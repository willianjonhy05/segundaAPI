from .models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class MyTokenObtainPairSerielizer