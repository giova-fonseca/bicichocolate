# Register your models here.
from django.contrib import admin

from sitio.models import Image, ChocolateType, Category, PointSale, Product, Flavor, PruebaFecha
from sorl.thumbnail.admin import AdminImageMixin
from .forms import ProductForm, PruebaFechaAdminForm

# class EmpAdmin(admin.ModelAdmin):
#   list_display = ('identificacion', 'nombre')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'image')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class InlineImage(admin.TabularInline):
    model = Image


#@admin.register(Product)
class ProductAdmin(AdminImageMixin, admin.ModelAdmin):
   
    form = ProductForm
    list_display = ("name", "description", "only_year")

class MyInlineModelAdmin(AdminImageMixin, admin.TabularInline):
    model = InlineImage


class MyModelAdmin(admin.ModelAdmin):
    inlines = [MyInlineModelAdmin]


# class ProductAdmin(admin.ModelAdmin):
#    inlines = [InlineImage]


#sadmin.site.register(Product, ProductAdmin)

class PruebaFechaAdmin(admin.ModelAdmin):
    
    def lavara(self, obj):
        return obj.lavara()    
    
    form = PruebaFechaAdminForm
    exclude = ['year_of_validity']


admin.site.register(Category, CategoryAdmin)
admin.site.register(ChocolateType)
admin.site.register(Flavor)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(PruebaFecha, PruebaFechaAdmin)
admin.site.register(PointSale)
