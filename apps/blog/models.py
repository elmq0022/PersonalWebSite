from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


class Tag(models.Model):
    tag = models.CharField(max_length=100)

    class Meta:
        ordering = ['tag']

    def __str__(self):
        return self.tag


class PublishedManager(models.Manager):
    def get_queryset(self):
        return (super()
            .get_queryset()
            .filter(published_date__lte=timezone.now())
            .filter(is_published=True)
        )

class Article(models.Model):
    edited_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    post = HTMLField()
    published_date = models.DateTimeField(null=True, blank=True)
    title = models.CharField(null=False, max_length=200)
    tags = models.ManyToManyField(Tag, related_name='articles')

    objects = models.Manager()
    published = PublishedManager()
    

    def save(self, *args, **kwargs):
        if self.is_published and self.published_date is None:
            self.published_date = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']
