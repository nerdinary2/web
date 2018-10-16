from django.urls import re_path,path
from . import views

urlpatterns = [
    re_path(r'index', views.index, name='index'),
    re_path(r'^figures$', views.figures_rows, name='figures_rows'),
    re_path(r'records', views.records_rows, name='records_row'),
    # re_path(r'article', views.article_rows, name='article_rows'),
    re_path(r'bangmok', views.bangmok_rows, name='bangmok_rows'),
    re_path(r'^article/(?P<pk>\w+)/$', views.articles, name = 'articles')

]