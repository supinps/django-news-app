from django.views.generic import ListView, TemplateView
from .models import Category,  SubCategory, Article

class HomePageView(ListView):
    model = Category
    context_object_name = 'category_list'
    template_name = 'home.html'

class CategoryPageView(ListView):
    model = Article
    queryset = Article.objects.all().order_by('-created_at')
    context_object_name = 'article_list'
    template_name = "category.html"
    paginate_by = 12

class TestPageView(ListView):
    model = Article
    queryset = Article.objects.all().order_by('-created_at')
    context_object_name = 'article_list'
    template_name = "test.html"
    paginate_by = 2
