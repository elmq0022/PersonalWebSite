from django.db import models
from django.core.cache import cache
from django.db.models.manager import ManagerDescriptor
from tinymce.models import HTMLField


class HtmlContentModel(models.Model):
    """
    Ensure only one model exists by always saving with a pk of 1.
    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
        self.set_cache()

    def delete(self, *args, **kwargs):
        """
        Do not delete.
        """
        pass

    def set_cache(self):
        cache.set(self.__class__.__name__, self)

    content = HTMLField()


class About(HtmlContentModel):
    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"

    def __str__(self):
        return "About Page"


class Resume(HtmlContentModel):
    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resume"

    def __str__(self):
        return "Resume Page"


class Projects(HtmlContentModel):
    class Meta:
        verbose_name = "Projects"
        verbose_name_plural = "Projects"

    def __str__(self):
        return "Projects Page"
