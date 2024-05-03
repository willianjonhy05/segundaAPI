from .models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class MyTokenObtainPairSerielizer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["full_name"] = user.profile.full_name
        token["username"] = user.username
        token["email"] = user.email
        token["bio"] = user.bio
        token["image"] = str(user.profile.image)
        token["verified"] = user.profile.verified
        return token
    
class RegisterSerielizer(serializers.Serializer):
    password = serializers.CharField()
        