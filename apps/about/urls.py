
from django.urls import path

from . import views

urlpatterns = [
    path('resume', views.ResumeView.as_view(), name='resume'),
    path('github', views.GitHubView.as_view(), name='github'),
    path('bio', views.BioView.as_view(), name='bio'),
]
