from api.views import category_list
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('category/', category_list),
]
