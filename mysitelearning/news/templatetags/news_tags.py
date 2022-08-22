from django import template
from news.models import Category
from django.db.models import *

register = template.Library()

@register.simple_tag()
def get_categ():
    return Category.objects.all()

@register.inclusion_tag('news/list_categories.html')
def g_categ():
    # categories = Category.objects.all()
    categories = Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)

    return {'categories': categories }