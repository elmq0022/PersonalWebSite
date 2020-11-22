from django.views import generic
from django.utils import timezone
from django.db.models import Prefetch

from .models import Article, Tag

class TagsView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'tags'
    queryset = Tag.objects.prefetch_related(
        Prefetch(
            'articles',
            queryset=Article.published.all()
        )
    )


class ArticleDetailView(generic.DetailView):
    template_name = 'blog/article.html'
    model = Article
    context_object_name = "article"

    
class ArticleListView(generic.ListView):
    template_name = 'blog/article_list.html'
    model = Article
    context_object_name = 'articles'
    queryset = Article.published.all()
