from rest_framework import serializers

from .models import About, Projects, Resume


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
