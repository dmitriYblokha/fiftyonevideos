from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import News, Category
from .forms import NewsForm
from .utils import MyMixin

def test(request):
    list_names = ['john1', 'mara2', 'gray3', 'yeltok4', 'john5', 'mara6', 'gray7', 'yeltok8', 'john9', 'mara10', 'gray11', 'yeltok12']
    paginator = Paginator(list_names, 2)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'news/test.html', {'page_obj': page_obj})

class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    mixin_prop = 'hello dima'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['pk']))
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['pk'], is_published=True).select_related('category')

class ViewNews(DetailView):
    model = News
    context_object_name = 'one_news'
    template_name = 'news/view_news.html'
    # pk_url_kwarg = 'ТОТ KWARQ, который задали в urls.py'

class AddNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    login_url = '/admin/'
    # success_url = reverse_lazy('home')


# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#     }
#     return render(request, 'news/index.html', context)


# def get_category(request, pk):
#     news = News.objects.filter(category_id=pk)
#     category = Category.objects.get(id=pk)
#     context = {
#         'news': news,
#         'category': category,
#     }
#     return render(request, 'news/category.html', context)


# def view_news(request, pk):
#     one_news = get_object_or_404(News, id=pk)
#     return render(request, 'news/view_news.html', { 'one_news': one_news })

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})
