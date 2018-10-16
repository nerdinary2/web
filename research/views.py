from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import TemplateView
from .models import Article, Figures, Bangmok, Records
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from .forms import HomeForm
from .processing import *
import pandas as pd



def index(request):
    figures = pd.read_sql('select * from figures where deleted = 0 and merged IS NULL', con=engine)
    # 한자 동명이인들을 찾아서 합칠 사람들을 본다.
    duplicates = figures[figures['chnname'].duplicated(keep=False)].sort_values('chnname')
    figs = Figures.objects.filter(manid__in=duplicates['manid']).order_by('chnname').exclude(deleted=1).exclude(checked=1)
    paginator = Paginator(figs, 30)
    page = request.GET.get('page')
    figures = paginator.get_page(page)
    all_columns = [ (f.verbose_name, f.name) for f in Figures._meta.get_fields() ]
    ret = ''
    print('')
    if request.method=='POST':
        form = HomeForm(data=request.POST)
        if form.is_valid() :
            merge = [i for i in form.cleaned_data['merge'].split(', ') if i != '']
            delete = [i for i in form.cleaned_data['delete'].split(', ') if i !='']
            check = [i for i in form.cleaned_data['check'].split(', ') if i != '']
            if len(merge) > 1:
                merge_request(merge)
            if len(delete) > 0:
                delete_request(delete)
            if len(check) > 0:
                check_request(check)
        ret = {'form':form, 'merge':merge,'delete':delete}
    return render(request, 'research/index.html',{'figs':figs, 'all_columns':all_columns,'figures':figures}, {'ret':ret})

def articles(request, pk):
    articles = Article.objects.filter(nameid__contains=pk).order_by('date')
    fig = Figures.objects.filter(manid__exact=pk)
    return render ( request,'research/article_detail.html',context={'articles':articles, 'pk':pk, 'fig':fig})



def article_rows(request):
    articles = Article.objects.all()
    return render(request, 'research/article_rows.html', {'articles': articles})

def bangmok_rows(request):
    bangmoks = Bangmok.objects.all()
    return render(request, 'research/bangmok_rows.html', {'bangmoks': bangmoks})

def figures_rows(request):
    figs = Figures.objects.all()
    return render(request, 'research/figures_rows.html', {'figures': figs})

def records_rows(request):
    recs = Records.objects.all()
    return render(request, 'research/records_rows.html', {'records': recs})


