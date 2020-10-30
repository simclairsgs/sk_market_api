from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Products
from .serializers import ProductSerializer


# Create your views here.
def api(request):
    return HttpResponse("Hello World!!")

@api_view(['GET'])
def product_detail(requests, Id):
    products = Products.objects.get(Product_Id=Id)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def product_list(request):
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def product_add(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Ok")
    return Response("Failed")

@api_view(['POST'])
def product_update(request, Id):
    products = Products.objects.get(Product_Id=Id)
    serializer = ProductSerializer(instance=products, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Ok")
    return Response("Failed")

@api_view(['DELETE'])
def product_delete(request, Id):
    products = Products.objects.get(Product_Id=Id)
    products.delete()
    return Response("Deleted Successfully...")
