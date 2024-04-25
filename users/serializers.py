from rest_framework import serializers
from .models import Task, CustomUser, Complexity, Status

class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('StatusTask',)


class TaskComplexitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Complexity
        fields = ('ComplexityTask',)


class TaskUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username',)


class TaskSerializer(serializers.ModelSerializer):

    author = TaskUserSerializer(read_only=True)
    complexity_bunch = TaskComplexitySerializer(read_only=True)
    status_bunch = TaskStatusSerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'


