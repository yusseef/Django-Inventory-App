from django.shortcuts import render,get_object_or_404 , redirect
from django.http import HttpResponse
from .forms import RecipeForm
# Create your views here.
from .models import Recipes
from django.contrib.auth.decorators import login_required
#def index(request):
 #   return HttpResponse('Recipes app')
    
@login_required
def recipe_list(request):
    query = Recipes.objects.filter(user = request.user)
    context = {'query': query}
    return render(request, 'recipes/RecipeList.html', context)


@login_required
def recipe_detail(request, id = None):
    query = get_object_or_404(Recipes, id = id, user = request.user)
    print(query)
    context = {'query': query}
    return render(request, 'recipes/RecipeDetail.html', context)


@login_required
def recipe_create(request):
    form = RecipeForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        form.save()
        form = RecipeForm()
        context['messages'] = 'data saved successfully'
        return redirect(obj.get_absolute_url())
   
    return render(request, 'recipes/RecipeCreateUpdate.html', context)

@login_required
def recipe_update(request, id = None):
    query = get_object_or_404(Recipes, id = id, user = request.user)
    form = RecipeForm(request.POST or None, instance = query)
    context = {'query': query, 
    'form': form}
    if form.is_valid():
        obj = form.save()
        context['messages'] = 'Data updated'
    

    return render(request, 'recipes/RecipeUpdateUpdate.html', context)