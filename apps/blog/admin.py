from django.contrib import admin

from .models import Article, Tag


class ArticleAdmin(admin.ModelAdmin):
    exclude = (
        "edited_date",
        "published_date",
    )

    fields = (
        "title",
        "tags",
        "post",
        "is_featured",
        "is_published",
    )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
