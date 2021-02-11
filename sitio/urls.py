import django.urls
from django.urls.conf import path
from sitio import views as sitio_views

urlpatterns = [
    path('', sitio_views.index, name='index'),
    path('galeria', sitio_views.galeria, name='galeria'),
    path('about', sitio_views.about, name='about'),
    path('contact', sitio_views.contact, name='contact'),
]
