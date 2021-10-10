#MODEL.PY
class PruebaFecha(models.Model):
    # Este campo ya esta creado en el model del proyecto.
    year_of_validity = models.DateField('Year of Validity', null=True, blank=True)


#FORMS
'''En el archivo forms.py agregar lo siguiente
'''

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


#ADMIN.PY
class PruebaFechaAdmin(admin.ModelAdmin):
    
    def lavara(self, obj):
        return obj.lavara()    
    
    form = PruebaFechaAdminForm
    exclude = ['year_of_validity']

admin.site.register(PruebaFecha, PruebaFechaAdmin)
