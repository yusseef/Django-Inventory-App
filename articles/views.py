from django.shortcuts import render, redirect, reverse
from .models import *
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.db.models import Q

# Create your views here.
def ArticListView(request):
    Query = Articles.objects.all()
    context = {'Query': Query}
    return render(request, 'articles/ArticleList.html', context)

@login_required
def ArticleCreateView(request):
    #Basic html create view
    form = ArticleForm()    
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            form = ArticleForm()
        

    context = {'form': form}
    return render(request,'articles/ArticleCreateView.html', context)


def ArticleView(request, id):
    try:
        Query = Articles.objects.get(id=id)
    except :
        raise Http404
    context = {'Query': Query}
    return render(request, 'articles/ArticleView.html', context)


def ArticleSearchView(request):
    #print(request.GET)
    QueryDict = request.GET
    PK = QueryDict.get('q') #<input type='text' name='q'/>
    Query = None
    if PK is not None:
        lookups = Q(title__contains=PK) | Q(content__icontains = PK)
        #QueryID = Articles.objects.get(id=PK) #Search by id
        Query = Articles.objects.all().filter(lookups)
        #print (QueryTitle)

    context = {"Query" : Query}
    return render(request, 'articles/ArticleSearchView.html', context)

