from django.contrib.auth.models import User

from rest_framework import serializers

from ..models import Task, TaskImage


class TaskImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskImage
        fields = '__all__'


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        exclude = ['last_login', 'is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    images = TaskImageSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = [
            'id', 'user', 'title', 'description', 'images', 
            'creationDateTime', 'dueDate', 'priority', 'isCompleted'
        ]

