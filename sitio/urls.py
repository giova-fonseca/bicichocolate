from django.urls.conf import path
from sitio import views as sitio_views

from django.contrib import admin
from django.urls import path, include
#from . import settings
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', sitio_views.index, name='index'),
    path('galeria', sitio_views.galeria, name='galeria'),
    #path('productos', sitio_views.productos, name='productos'),
    path('productos', sitio_views.productos, name='productos'),
    path('upload_image', sitio_views.upload_image, name='upload_image'),
    path('image_gallery', sitio_views.image_gallery, name='image_gallery'),
    path('puntos_ventas', sitio_views.puntos_ventas, name='puntos_ventas'),
    path('Galeria', sitio_views.slider, name='galeriaProductos'),
    # path('slider/<int:pk>', sitio_views.ProductSlider.as_view(),
    #      name='Images_Product'),
    path('slider2/<int:pk>/', sitio_views.slider2, name='ImagesProduct'),

    path('about', sitio_views.about, name='about'),
    path('contact', sitio_views.contact, name='contact'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
