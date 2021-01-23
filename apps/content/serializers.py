from .models import About, Resume, Projects
from rest_framework import serializers


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ("content",)


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ("content",)


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ("content",)
