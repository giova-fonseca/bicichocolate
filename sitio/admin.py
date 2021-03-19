# Register your models here.
from django.contrib import admin

from sitio.models import Image, POS, ChocolateType, Category, Product, Flavor
from sorl.thumbnail.admin import AdminImageMixin
# class EmpAdmin(admin.ModelAdmin):
#   list_display = ('identificacion', 'nombre')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class InlineImage(admin.TabularInline):
    model = Image


class ProductAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('name', 'description')


class MyInlineModelAdmin(AdminImageMixin, admin.TabularInline):
    model = InlineImage


class MyModelAdmin(admin.ModelAdmin):
    inlines = [MyInlineModelAdmin]


# class ProductAdmin(admin.ModelAdmin):
#    inlines = [InlineImage]


#sadmin.site.register(Product, ProductAdmin)


admin.site.register(Category, CategoryAdmin)
admin.site.register(ChocolateType)
admin.site.register(Flavor)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(POS)
