from django import forms

from .models import Recipe, RecipeIngredient

class RecipeForm(forms.ModelForm):
    required_css_class = 'required-field'
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",
    "placeholder": "Recipe name"}))
    # name = forms.CharField(help_text='this is help!')
    #description = forms.CharField(widget=forms.Textarea(attrs={"rows":3}))
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'directions']

    '''
        another way of doing this is tho make use of the constructors
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'rows':3})
        self.fields['directions'].widget.attrs.update({'rows':3})
        self.fields['name'].widget.attrs.update({'class': 'form-control-2'})
        self.fields['name'].label ='that boy'
        self.fields['name'].help_text='this here is your help <a href="/contact">contact us</a>'
    
class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['name', 'quantity', 'unit', 'directions']