from rest_framework import serializers
from django.contrib.auth.models import User

from .models import JobCircular


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCircular
        fields = 'job_title', 'publish_date', 'deadline', 'location'

# Admin User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']