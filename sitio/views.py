from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, View
from django.views import generic
from django.urls import reverse_lazy
from django.core import serializers
from django.http import JsonResponse


# Create your views here.


def index(request):
    return render(request, 'sitio/index.html')


def about(request):
    return render(request, 'sitio/about.html')


def producto(request):
    productos = Product.objects.all()
    return render(request, 'sitio/product.html', {'products': productos})


def productos(request):
    productos = Product.objects.all()
    return render(request, 'sitio/products.html', {'products': productos})


def slider(request):
    product = Product.objects.first()
    context = {'product': product}
    return render(request, 'sitio/productsimage.html', context)
    # return render(request, 'sitio/modal.html', context)


class ProductSlider(generic.ListView):
    model = Product

    product = Product.objects.first()
    context = {'product': product}

    template_name = "sitio/modal.html"
    context_object_name = "obj"
    success_url = reverse_lazy("sitio:productos")
    success_message = "Listado exitoso"


def slider2(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'sitio/productsimage.html', context)


def contact(request):
    return render(request, 'sitio/contact.html')


def galeria(request):
    return render(request, 'sitio/galeria.html')


def upload_image(request):
    if request.method == 'GET':
        return render(request, 'sitio/upload_image.html')
    elif request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = Image(image=form.cleaned_data["image"],
                              name=form.cleaned_data["name"]
                              )
            new_image.save()
            return HttpResponseRedirect('/sitio/image_gallery')


def image_gallery(request):
    images = Image.objects.all()
    return render(request, 'sitio/image_gallery.html', {'images': images})


def puntos_ventas(request):
    puntosventas = POS.objects.all()
    return render(request, 'sitio/pos.html', {'puntosventas': puntosventas})


class PictureView(View):
    def get(self, request):
        qs = Product.objects.all()
        data = serializers.serialize('json', qs)
        return JsonResponse({'data': data}, safe=False)
