from django.db.models import Prefetch, query
from rest_framework import generics, pagination
from rest_framework.pagination import PageNumberPagination

from .models import Article, Tag
from .serializers import ArticleListSerializer, ArticleSerializer, TagSerializer


class TagListView(generics.ListAPIView):
    queryset = Tag.objects.filter(article__is_published=True).distinct()
    serializer_class = TagSerializer


class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.published.all()
    serializer_class = ArticleSerializer


class ArticleListPagination(PageNumberPagination):
    page_size = 10


class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleListSerializer
    pagination_class = ArticleListPagination

    def get_queryset(self):
        queryset = Article.published.all()
        featured = self.request.query_params.get("featured", None)
        if featured is not None:
            if featured == "true":
                queryset = queryset.filter(is_featured=True)
            if featured == "false":
                queryset = queryset.filter(is_featured=False)
        return queryset
