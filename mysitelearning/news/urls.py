from django.urls import path
from .views import *

urlpatterns = [
    # path('', index, name='home'),
    path('', HomeNews.as_view(), name='home'),
    # path('category/<int:pk>/', get_category, name='category'),
    path('category/<int:pk>/', NewsByCategory.as_view(), name='category'),
    # path('news/<int:pk>/', view_news, name='view_news'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    # path('news/add-news/', add_news, name='add_news'),
    path('news/add-news/', AddNews.as_view(), name='add_news'),
    path('test/', test, name='test'),
]