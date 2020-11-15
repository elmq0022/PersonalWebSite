from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    exclude = (
        "edited_date",
        "published_date",
    )

    fields = (
        "title",
        "post",
        "is_published",
    )


admin.site.register(Article, ArticleAdmin)
