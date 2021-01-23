from django.core.management.base import BaseCommand, CommandError
from apps.content.models import About, Resume, Projects


class Command(BaseCommand):
    help = (
        "creates the intial instances of the content instances"
        "so they can be edited in the admin"
    )

    def handle(self, *args, **options):
        about, _ = About.objects.get_or_create(pk=1)
        about.save()

        resume, _ = Resume.objects.get_or_create(pk=1)
        resume.save()

        projects, _ = Projects.objects.get_or_create(pk=1)
        projects.save()
