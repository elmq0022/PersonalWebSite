from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path("about/", views.AboutView.as_view()),
    path("projects/", views.ProjectsView.as_view()),
    path("resume/", views.ResumeView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
