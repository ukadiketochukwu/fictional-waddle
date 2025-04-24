from rest_framework import serializers
from .models import LogisticUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = LogisticUser
        fields = ['username', 'email', 'password', 'role']

    def create(self, validated_data):
        user = LogisticUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data['role'],
        )
        return user

