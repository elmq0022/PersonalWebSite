from django.contrib import admin

from .models import About, Projects, Resume


class HtmlContentModelAdmin(admin.ModelAdmin):
    """
    Prevents Django admin users deleting the singleton or adding extra rows.
    """

    actions = None  # Removes the default delete action.

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


@admin.register(About)
class AboutAdmin(HtmlContentModelAdmin):
    pass


@admin.register(Projects)
class ProjectsAdmin(HtmlContentModelAdmin):
    pass


@admin.register(Resume)
class ResumeAdmin(HtmlContentModelAdmin):
    pass
