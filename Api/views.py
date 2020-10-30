from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Products,Login,Sales,Stock,Billing
from .serializers import ProductSerializer,LoginSerializer,SalesSerializer,StockSerializer,BillingSerializer


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


@api_view(['GET'])
def Employee_list(request):
        login = Login.objects.all()
        serializer = LoginSerializer(login, many=True)
        return Response(serializer.data)



@api_view(['GET'])
def Billing_list(request):
        bill = Billing.objects.all()
        serializer = BillingSerializer(bill, many=True)
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


@api_view(['POST'])
def Stock_update(request, Id):
    stock = Stock.objects.get(Product_Id=Id)
    serializer =StockSerializer(instance=stock, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Ok")
    return Response("Failed")


@api_view(['POST'])
def Employee_update(request, Id):
    employee = Login.objects.get(Employee_Id=Id)
    serializer = LoginSerializer(instance=employee, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Ok")
    return Response("Failed")

@api_view(['DELETE'])
def product_delete(request, Id):
    products = Products.objects.get(Product_Id=Id)
    products.delete()
    return Response("Deleted Successfully...")

@api_view(['POST'])
def Login_Add_Users(request):
    serializer=LoginSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("OK")
    return Response("Failed")

@api_view(['DELETE'])
def Employee_Delete(request,ID):
    Employee=Login.objects.get(Employee_Id=ID)
    Employee.delete()
    return Response('Deleted Successfully')

@api_view(['POST'])
def Stock_Manage(request):
    serializer=StockSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Successfully')
    return Response('Failed')


@api_view(['GET'])
def View_One_Stock(request,ID):
    stock=Stock.objects.get(Product_Id=ID)
    serializer=StockSerializer(stock,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def View_All_Stock(request):
    stock=Stock.objects.all()
    serializer=StockSerializer(stock,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def Billing_Product(request):
    serializer=BillingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Successfully")
    return Response("Failed")


@api_view(['POST'])
def Total_Sales(request):
    Sales=Billing.objects.get.all()
    serializer = SalesSerializer(instance=Sales,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Ok")
    return Response("Failed")

@api_view(['GET'])
def Get_Sales_Of(request,date):
    sales=Sales.objects.get(Date=date)
    serializer=SalesSerializer(sales,many=False)
    return Response(serializer.data)


@api_view(['GET'])
def Get_All_Sales(request):
    #sales=Sales.objects.get.all()
    alls=Sales.objects.all()
    serializer=SalesSerializer(alls,many=True)
    return Response(serializer.data)
    



