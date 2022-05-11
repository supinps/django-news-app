from django import template
from ..models import Article, Category

import random

register = template.Library()

@register.simple_tag
def get_categories():
    categories = Category.objects.all()
    return categories

@register.simple_tag
def get_postcount(categ):
    count = Article.objects.filter(subcategory__in=categ.subcateogories.all()).count()
    return count

@register.simple_tag
def get_randomitems(item, count):
    listitem = list(item)
    randomitems = []
    for i in range(count):
        randomitem = random.choice(listitem)
        randomitems.append(randomitem)
        listitem.remove(randomitem)
    return randomitems

@register.simple_tag
def get_featurepostitems():
    articles_news = Article.objects.filter(subcategory__in = Category.objects.get(name='News').subcateogories.all()).order_by('-created_at')[:2]
    articles_views = Article.objects.filter(subcategory__in = Category.objects.get(name='Views').subcateogories.all()).order_by('-created_at')[:2]
    articles = list(articles_news | articles_views)
    random.shuffle(articles)
    featured = dict(enumerate(articles))
    return featured

@register.simple_tag
def get_posts(subcat):
    _articles = Article.objects.filter(subcategory = subcat).order_by('-created_at')[:4]
    articles = dict(enumerate(_articles))
    return articles

@register.simple_tag
def get_postsall(categ):
    _articles = Article.objects.filter(subcategory__in=categ.subcateogories.all()).order_by('-created_at')[:4]
    articles = dict(enumerate(_articles))
    return articles

@register.simple_tag
def get_toparticles(subcateg, count):
    articles = Article.objects.filter(subcategory=subcateg).order_by('-created_at')[:4]
    return articles

@register.simple_tag
def get_topall(count):
    articles = Article.objects.all().order_by('-created_at')[:count]
    return articles

@register.inclusion_tag('topfour.html')
def topfour(subcateg):
    articles = Article.objects.filter(subcategory=subcateg).order_by('-created_at')[:4]
    return {'articles':articles}

@register.inclusion_tag("topfour.html")
def topfourall(categ):
    articles = Article.objects.filter(subcategory__in=categ.subcateogories.all()).order_by('-created_at')[:4]
    return {'articles':articles}
