from django.db import models
from tinymce.models import HTMLField


class ArticleModel(models.Model):
    title = models.CharField(null=False, max_length=200)
    date = models.DateField()
    post = HTMLField()

    def __str__(self):
        return self.title
