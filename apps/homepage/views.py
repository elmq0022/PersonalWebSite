from django.views.generic import TemplateView

from apps.blog.models import Article


class HomePageView(TemplateView):
    template_name = "hompage/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_five_articles'] = Article.objects.order_by('-published')[:5]
        return context
        
