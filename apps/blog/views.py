from django.db.models import Prefetch
from rest_framework import generics

from .models import Article, Tag
from .serializers import ArticleSerializer, TagSerializer


class TagListView(generics.ListAPIView):
    queryset = Tag.objects.prefetch_related(
        Prefetch(
            'articles',
            queryset=Article.published.all()
        )
    )
    serializer_class = TagSerializer


class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.published.all()
    serializer_class = ArticleSerializer


class ArticleListView(generics.ListAPIView):
    queryset = Article.published.all()
    serializer_class = ArticleSerializer
