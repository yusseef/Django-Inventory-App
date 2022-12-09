from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def ArticListView(request):
    Query = Articles.objects.all()
    context = {'Query': Query}
    return render(request, 'articles/ArticleList.html', context)

def ArticleCreateView(request):
    #Basic html create view
    context = {}
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Query = Articles.objects.create(title=title, content=content)
        context['Query'] = Query
        context['created'] = True      
    
    return render(request,'articles/ArticleCreateView.html', context)


def ArticleView(request, id):
    Query = Articles.objects.get(id=id)
    context = {'Query': Query}
    return render(request, 'articles/ArticleView.html', context)


def ArticleSearchView(request):
    #print(request.GET)
    QueryDict = request.GET
    PK = QueryDict.get('q') #<input type='text' name='q'/>
    Query = None
    if PK is not None:
        #QueryID = Articles.objects.get(id=PK) #Search by id
        Query = Articles.objects.all().filter(title__contains=PK)
        #print (QueryTitle)

    context = {"Query" : Query}
    return render(request, 'articles/ArticleSearchView.html', context)

