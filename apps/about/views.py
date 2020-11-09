"""

"""


from django.views import generic


class ResumeView(generic.TemplateView):
    template_name = 'about/resume.html'


class BioView(generic.TemplateView):
    template_name = 'about/bio.html'


class GitHubView(generic.TemplateView):
    template_name = 'about/github.html'

