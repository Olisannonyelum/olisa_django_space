from django.db import models
from django.conf import settings
from .validators import validate_unit_of_measure
# Create your models here.
from .utils import number_str_to_float
import pint
from django.urls import reverse

class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    directions= models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        # return  reverse('detail', kwargs={'id':self.id})
        """
            by introducing the app_name in the urls.py we have the 
            reverse modefies as the below
        """
        
        return  reverse('recipes:detail', kwargs={'id':self.id})

    def get_hx_url(self):
        return  reverse('recipes:hx-detail', kwargs={'id':self.id})

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)
    quantity = models.CharField(max_length=50)
    quantity_as_float = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=50, validators=[validate_unit_of_measure])
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)   

    def get_absolute_url(self):
        return self.recipe.get_absolute_url() #this will work just find as long as recipe is not empty

    """ 
        self.recipe is a foreing key to the class recipe in django that make self.recipe
        an instance of the class recipe, that is why we a able to access the method in the 
        recipe class
    """



    def convert_to_system(self, system="mks"):
        if self.quantity_as_float is None:
            return None
        ureg = pint.UnitRegistry(system=system)
        measurement = self.quantity_as_float * ureg[self.unit]
        print('is', measurement)
        return measurement #.to_base_units()


    def as_mks(self):
        #meter, kilogram, second
        measurement = self.convert_to_system(system='mks')
        return measurement
        
    def as_imperial(self):
        #miles, pounds, seconds
        measurement = self.convert_to_system(system='imperial')
        return measurement   
        
        """

            the fun part of this is that we can add this method as readonly part in the admin as if it is a field

        """



    def save(self, *args, **kwargs):
        """
        what we do here is kind of  overwrite the save method
        by prividing a space for nessery editing befor the actuall save is done

        we call upon the quantity and pass it into the number_str_to_float function 
        then we assign the return value to the quantity_as_float field
        """
        qty = self.quantity  
        qty_as_float, qty_as_float_success = number_str_to_float(qty)
        if qty_as_float_success:
            self.quantity_as_float = qty_as_float
        else:
            self.quantity_as_float = None
        super().save(*args, **kwargs)
