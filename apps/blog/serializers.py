from django.utils.text import Truncator
from rest_framework import serializers

from .models import Article, Tag


class ArticleListSerializer(serializers.ModelSerializer):
    published_date = serializers.DateTimeField(format="%Y-%m-%d at %I:%M%p")
    short_description = serializers.SerializerMethodField()

    def get_short_description(self, obj):
        t = Truncator(obj.post)
        return t.words(30, html=True)

    class Meta:
        model = Article
        fields = [
            "pk",
            "published_date",
            "short_description",
            "title",
        ]


class ArticleSerializer(serializers.ModelSerializer):
    published_date = serializers.DateTimeField(format="%Y-%m-%d at %I:%M%p")

    class Meta:
        model = Article
        fields = [
            "is_featured",
            "pk",
            "post",
            "published_date",
            "title",
        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("name", "pk")
