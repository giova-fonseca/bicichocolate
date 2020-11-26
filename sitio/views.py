from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'sitio/index.html')

def about(request):
    return render(request,'sitio/about.html')

def contact(request):
    return render(request,'sitio/contact.html')

def galeria(request):
    return render(request,'sitio/galeria.html')