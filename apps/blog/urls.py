from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path("article/", views.ArticleListView.as_view()),
    path("tag/", views.TagListView.as_view()),
    path("article/<int:pk>/", views.ArticleDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)