from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

# Create your views here.


def index(request):
    return render(request, 'sitio/index.html')


def about(request):
    return render(request, 'sitio/about.html')


def productos(request):
    productos = Product.objects.all()
    return render(request, 'sitio/products.html', {'products': productos})


def slider(request):
    product = Product.objects.first()
    context = {'product': product}
    return render(request, 'sitio/productsimage.html', context)


def slider2(request):
    product = Product.objects.first()
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
