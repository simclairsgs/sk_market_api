from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Products,Login,Sales,Stock,Billing
from .serializers import ProductSerializer,LoginSerializer,SalesSerializer,StockSerializer,BillingSerializer


# sample test api
def api(request):
    return HttpResponse("Hello World!!")

# Login Auth api
@api_view(['POST'])
def login_auth(request):
    employee_id = request.data.get('emp_id')
    employee_pwd = request.data.get('emp_pass')
    try:
        emp_data = Login.objects.get(Employee_Id = employee_id)
        if(emp_data.Password == employee_pwd):
            serializer = LoginSerializer(emp_data,many=False)
            return Response(serializer.data)
    except:
        return Response("AuthFailed")
    return Response("AuthFailed")


# Products api views 

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

# Employee/Login api views

@api_view(['GET'])
def employee_list(request):
        login = Login.objects.all()
        serializer = LoginSerializer(login, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def login_add_users(request):
    serializer=LoginSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("OK")
    return Response("Failed")


@api_view(['POST'])
def employee_update(request, Id):
    employee = Login.objects.get(Employee_Id=Id)
    serializer = LoginSerializer(instance=employee, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Ok")
    return Response("Failed")


@api_view(['DELETE'])
def employee_delete(request,Id):
    Employee=Login.objects.get(Employee_Id=Id)
    Employee.delete()
    return Response('Deleted Successfully')


# Stock api views

@api_view(['POST'])
def stock_add_detail(request):
    serializer=StockSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Successfully')
    return Response('Failed')


@api_view(['GET'])
def view_one_stock(request,Id):
    stock=Stock.objects.get(Product_Id=Id)
    serializer=StockSerializer(stock,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def view_all_stock(request):
    stock=Stock.objects.all()
    serializer=StockSerializer(stock,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def stock_update(request, Id):
    stock = Stock.objects.get(Product_Id=Id)
    serializer =StockSerializer(instance=stock, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Ok")
    return Response("Failed")


# Billing api views

@api_view(['GET'])
def billing_list(request):
        bill = Billing.objects.all()
        serializer = BillingSerializer(bill, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def billing_product(request):
    serializer=BillingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Successfully")
    return Response("Failed")


# Sales api views

@api_view(['POST'])
def total_sales(request):
    Sales=Billing.objects.get.all()
    serializer = SalesSerializer(instance=Sales,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Ok")
    return Response("Failed")

@api_view(['GET'])
def get_sales_of(request,date):
    sales=Sales.objects.get(Date=date)
    serializer=SalesSerializer(sales,many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_sales(request):
    alls=Sales.objects.all()
    serializer=SalesSerializer(alls,many=True)
    return Response(serializer.data)
    



