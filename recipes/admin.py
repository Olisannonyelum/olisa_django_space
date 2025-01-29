from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.
from .models import RecipeIngredient, Recipe
from article.admin import articleInline
""" 
    here i include the articleinline in the admin.py of the 
    article folder i try adding it as an inline to the user
    models but it refuse to work, it look like i can only inlude
    it in one location at a time so i did everything in one location

"""

user = get_user_model()

admin.site.unregister(user) #here we unregister the user so as to applie change to the user by using admin.ModelAdmin

class Recipeinline(admin.StackedInline):
    model = Recipe #here we are adding the recipe as inline 
    # fields = ['name', 'quantity', 'unit', 'directions']
    extra = 0

class useradmin(admin.ModelAdmin):
    inlines = [Recipeinline, articleInline] #here we include the recipe as an inline to the user 



class RecipeIngredientInline(admin.StackedInline):#this help to put the recipeingredient to the same page of the of the recipe it is related to 
    #no need for admin.TabulaInline
    model = RecipeIngredient
    readonly_fields = ['quantity_as_float', 'as_mks', 'as_imperial']
    # fields = ['name', 'quantity', 'unit', 'directions']
    extra = 0

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline ]
    list_desplay = ['name','user', 'directions']
    raw_id_fields = ['user']
    readonly_fields = ['timestamp', 'updated']

admin.site.register(user, useradmin) # here we re-register the user after making change to itop

admin.site.register(Recipe, RecipeAdmin)
