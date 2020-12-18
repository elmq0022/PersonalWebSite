from .models import Article, Tag
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):

    published_date = serializers.DateTimeField(format="%Y-%m-%d at %I:%M%p")

    class Meta:
        model = Article
        fields = [
            "pk",
            "post",
            "published_date",
            "title",
        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag',)
