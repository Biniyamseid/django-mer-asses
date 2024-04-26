from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Role

User = get_user_model()

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']

class UserRegistrationSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'roles')

    def create(self, validated_data):
        roles_data = validated_data.pop('roles')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        for role_data in roles_data:
            role, _ = Role.objects.get_or_create(name=role_data['name'])
            user.roles.add(role)
        user.save()
        return user
class UserSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'roles')