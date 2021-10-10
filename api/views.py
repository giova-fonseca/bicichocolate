from sitio.models import Category
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from api.serializers import CategorySerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def category_list(request):
    if request.method == 'GET':
        categorys = Category.objects.all()
        serializer = CategorySerializer(categorys, many=True)
        return JsonResponse(serializer.data, safe = False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data= data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status =201)
        return JsonResponse(serializer.errors, status=400)
        
