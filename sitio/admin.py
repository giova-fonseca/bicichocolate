# Register your models here.
from django.contrib import admin

from sitio.models import Image, POS, ChocolateType, Category, Product, Flavor

# class EmpAdmin(admin.ModelAdmin):
#   list_display = ('identificacion', 'nombre')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Category, CategoryAdmin)
admin.site.register(ChocolateType)
admin.site.register(Flavor)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(POS)
