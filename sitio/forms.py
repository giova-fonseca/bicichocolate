from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.forms import fields
from django.forms.widgets import Widget
from .models import *
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'name']

class ProductForm(forms.ModelForm):     

    class Meta:
        model = Product
        fields = ['category','chocolateType','flavor','name','description','imagen','price','is_active','year_of_validity']
        #exclude =['year_of_validity']
        #fields = '__all__'


from django.utils.dateparse import parse_date

class PruebaFechaAdminForm(forms.ModelForm):
    YEAR_CHOICES = []
    for r in range(2015, (datetime.datetime.now().year+2)):
        YEAR_CHOICES.append((r,r))

    tmp_year_validity = forms.ChoiceField(choices=YEAR_CHOICES)    
                                     

    def save(self, *args, **kwargs):
    
        tmp = self.cleaned_data['tmp_year_validity']
        
        tmp_PruebaFecha = super(PruebaFechaAdminForm,self).save(commit=False)        
        temp_date = parse_date(str(str(tmp) + "-01-02"))                
        
        tmp_PruebaFecha.year_of_validity = temp_date
        tmp_PruebaFecha.save()
        return tmp_PruebaFecha
        
        #super(PruebaFechaAdminForm, self).save(*args, **kwargs)                        

 
    class Meta:
        model = PruebaFecha
        exclude = ['year_validity']
