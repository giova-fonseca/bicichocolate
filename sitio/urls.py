import django.urls
from django.urls.conf import path
from sitio import views as sitio_views

urlpatterns = [
    path('',sitio_views.index, name='index')
]
