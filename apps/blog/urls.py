from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path("articles/", views.ArticleListView.as_view()),
    path("tags/", views.TagListView.as_view()),
    path("articles/<int:pk>/", views.ArticleDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)