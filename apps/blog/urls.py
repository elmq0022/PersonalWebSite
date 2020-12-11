from django.urls import path

from . import views
from . import api

app_name = 'blog'

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="list"),
    path("tags", views.TagsView.as_view(), name="tags"),
    path("<int:pk>", views.ArticleDetailView.as_view(), name="detail"),
]
