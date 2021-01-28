from rest_framework import generics
from rest_framework import parsers
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser

from .models import Article, Tag
from .serializers import ArticleListSerializer, ArticleSerializer, TagSerializer
from django.db.models import Q


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
    parser_classes = [JSONParser]

    def get_queryset(self):
        filters = Q()

        featured = self.request.query_params.get("featured", None)
        if featured is not None:
            if featured == "true":
                filters &= Q(is_featured=True)
            if featured == "false":
                filters &= Q(is_featured=False)

        tags = self.request.query_params.get("tags", None)
        if tags is not None:
            try:
                tags = tuple(int(x) for x in tags.split(","))
                filters &= Q(tags__in=tags)
            except:
                pass

        search = self.request.query_params.get("search", None)
        if search is not None:
            filters &= Q(post__icontains=search)

        return Article.published.filter(filters)
