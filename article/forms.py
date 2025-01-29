from django import forms
from .models import article



class article_form(forms.ModelForm):
    class Meta:
        model = article
        fields = ['title', 'content']

    def clean(self):
        data = self.cleaned_data
        qs = article.objects.filter(title__icontains = data.get('title'))
        if qs.exists():
            self.add_error("title", f"{data.get('title')} id already in use.")
        return data
                    # qs = article.objects.filter(<fiel name to search>__icontains= <field name >)
                    # if qs.exists():
                        

class article_form_old(forms.Form):
    title = forms.CharField()
    content = forms.CharField()


    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     print(cleaned_data)
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == "the office":
    #         raise forms.ValidationError('this title is taken.')#this help to clean the data by preventing similar that from occouring
    #     #just like preventing user from entering the a user name that that already exist in the database
    #     print(title)
    #     return title 
    
    def clean(self):
         cleaned_data = self.cleaned_data
         title = cleaned_data.get('title')
         if title.lower().strip() == "the office":
             self.add_error('title', 'this title is taken.')
             # the same shit as as the validationerror
         print('all data', cleaned_data)
         return cleaned_data

#this two function above clean the data entering the form before entering the database 
#if error is pockup the data entered the form is discade and prevented from entering the database 

# what i dont understand here is that between self.add_error and raise forms.validationerror
# one of them is a field error but i dont quite understand this error


#now the best way to clean data, that is to prevent the same data to occure in the database
# this is done using search quary as in .....>
