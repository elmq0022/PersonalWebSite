from .models import Article, Tag
from rest_framework import routers, serializers, viewsets


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = [
            "title",
            "post",
        ]


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.published
    order = ("-published_date")
    serializer_class = ArticleSerializer


