from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


class Article(models.Model):
    edited_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    post = HTMLField()
    published_date = models.DateTimeField(null=True, blank=True)
    title = models.CharField(null=False, max_length=200)

    @classmethod
    def published_articles(cls):
        return (cls.objects
            .order_by('-published_date')
            .filter(published_date__lte=timezone.now())
            .filter(is_published=True)
        )

    def save(self, *args, **kwargs):
        if self.is_published and self.published_date is None:
            self.published_date = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
