from django import forms

from .models import Recipe, RecipeIngredient

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'directions']
    
class RecipeIngredientform(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['name', 'quantity', 'unit', 'directions']