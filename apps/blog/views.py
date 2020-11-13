from django.views import generic
from django.utils import timezone

from .models import Article


class ArticleDetailView(generic.DetailView):
    template_name = 'blog/article.html'
    model = Article
    context_object_name = "article"

    
class ArticleListView(generic.ListView):
    template_name = 'blog/article_list.html'
    model = Article
    context_object_name = 'articles'
    queryset = Article.published_articles
