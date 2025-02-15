from django.shortcuts import redirect, render ,get_object_or_404
from .models import  Recipe, RecipeIngredient 
from django.contrib.auth.decorators import login_required
from .form import RecipeForm, RecipeIngredientForm
from django.forms.models import modelformset_factory
from django.http import HttpResponse
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


# .........................................................................



    def recipe_detail_hx_view(request, id=None):
        try:
            obj = Recipe.object.get(id=id, user=request.user)
        except:
            obj = None
        if obj is None:
            return HttpResponse("Not found")

        context= {
            "object":obj
        }
        return render(request, 'recipes/partials/detail.html', context)



# ..........................................................................

@login_required
def recipe_create_view(request):
    form = RecipeForm(request.POST or None)
    context= {
        "form":form
    }
    if form.is_valid():
        obj = form.save(commit=False)#
        obj.user = request.user #that i did here was to recreat the user, or say i overwrite the user 
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request,"recipes/create_update.html", context)


@login_required  
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    '''
        for me why the object is pre-fill is that the intention is to update the form
        and by so doing we create a form and that form to be updata is call upon (which is the obj as we see above)
        and is use to pre-fill the form -----> that is why we didn't assign value to the user in the recipe_update_view function's
        becase this model use to pre-fill have it user field assing already(this is an already created) we just updating it

    '''
    form = RecipeForm(request.POST or None, instance= obj)
    # print(f'this here is the request post.......{request.POST}')
    '''
        the instance is use to pre-fille the form with the obj
        note 
        also there is other way to pre-fill a form using 
        the argument 'initial' as is 
            form = RecipeForm(request.POST or None, initial={'name':name, 'direction':direction})

    '''
    # ingredient_forms = []
    # for ingredients in obj.recipeingredient_set.all():
    #     ingredient_forms.append(
    #         RecipeIngredientform(request.POST, or None, instance=ingredients)
    #     )


    #obj = Recipe.objects.filter(user=request.user)
    '''
        the new way of doing multiple form in a view 
    '''
    RecipeIngredientFormset = modelformset_factory(RecipeIngredient, form=   RecipeIngredientForm,
    extra=0) #what we did here is to create the formset class not initiallizing

    qs = obj.recipeingredient_set.all()

    formset = RecipeIngredientFormset(request.POST or None, queryset=qs)
    # what we did here is to initialize the formet, note the number of form depend on the number of queryset avalable

    context= {
        "form":form,
        "object":obj,
        # "ingredient_form": ingredient_forms,
        "formset":formset 
    }
    if all([form.is_valid(), formset.is_valid()]): 
    # if all([form.is_valid() for form in ingredient_forms]):
    
        parent = form.save(commit=False)
        parent.save()
        for form in formset:
            child = form.save(commit=False)
            # if child.recipe is None:
            #     print('...................added new parent..................')
            child.recipe=parent
            child.save()
        # child = form2.save(commit=False)#this is use for saving the data without it being save into the model
        
        context['massage'] = "data saved"
    if request.htmx:
        return render(request, "recipes/partials/forms.html", context)
    return render(request, "recipes/create_update.html", context)
    '''
        not also we can use formset.save(), but we whent through iteration each
        form in the formset and save them one after the other and to make sure 
        that the recipe field is not None if None we re-assing them
    ''' 