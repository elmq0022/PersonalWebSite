from django.views import generic
from .models import ArticleModel


class ArticleDetailView(generic.DetailView):
    template_name = 'blog/article.html'
    model = ArticleModel
    context_object_name = "article"

    
    
