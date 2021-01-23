from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import About, Projects, Resume
from .serializers import AboutSerializer, ProjectsSerializer, ResumeSerializer


class RetrieveContentView(generics.RetrieveAPIView):
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, pk=1)
        self.check_object_permissions(self.request, obj)
        return obj


class AboutView(RetrieveContentView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class ProjectsView(RetrieveContentView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class ResumeView(RetrieveContentView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
