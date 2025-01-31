from django.shortcuts import redirect, render ,get_object_or_404
from .models import  Recipe
from django.contrib.auth.decorators import login_required
from .form import RecipeForm
""" 
    let see how make use of the get_object_or_404
    what this does is that it let us make a data query base on the login user
    this may replace that we have previousely as in 
    |
    --> gs = Recipe.object.filter(user=request.user)
"""


# Create your views here.

#the concept of CRUD ->Create, Retrueve, Update & Delete

@login_required
def recipe_list_view(request):
    qs = Recipe.objects.filter(user=request.user)#making the loockup to be base on the user 
    context = {
        "object_list":qs

    }
    return render(request, 'recipes/list.html', context)

@login_required
def recipe_detail_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)

    """
        what this does is that it let us to make a seach base on the field id but 
        base on the user login , that is only user that matchies that id
    """

    #obj = Recipe.objects.filter(user=request.user)
    context= {
        "object":obj
    }
    return render(request, 'recipes/detail.html', context)

@login_required
def recipe_create_view(request):
    form = RecipeForm(request.POST or None)
    context= {
        "form":form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user #that i did here was to recreat the user, or say i overwrite the user 
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request,"recipes/create_update.html", context)


@login_required  
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    form = RecipeForm(request.POST or None, instance= obj)

    #obj = Recipe.objects.filter(user=request.user)
    context= {
        "form":form,
        "object":obj
    }
    if form.is_valid():
        form.save()
        context['massage'] = "data saved"
    return render(request, "recipes/create_update.html", context)