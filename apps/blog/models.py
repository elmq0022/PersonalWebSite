from django.db import models
from tinymce.models import HTMLField


class Article(models.Model):
    title = models.CharField(null=False, max_length=200)
    published = models.DateField()
    post = HTMLField()

    def __str__(self):
        return self.title
