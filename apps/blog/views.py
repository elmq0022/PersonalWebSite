from django.views import generic
from .models import Article


class ArticleDetailView(generic.DetailView):
    template_name = 'blog/article.html'
    model = Article
    context_object_name = "article"

    
class ArticleListView(generic.ListView):
    template_name = 'blog/article_list.html'
    model = Article
    context_object_name = 'articles'
    queryset = Article.objects.order_by('-published')

