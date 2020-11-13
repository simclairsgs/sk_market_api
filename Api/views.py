from django.shortcuts import render
from django.http import HttpResponse,QueryDict,JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Products,Login,Sales,Stock,Billing,Tax
from .serializers import ProductSerializer,LoginSerializer,SalesSerializer,StockSerializer,BillingSerializer,TaxSerializer


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


@api_view(['POST'])
def change_password(request):
    emp_id = request.data.get('emp_id')
    emp_pwd_old = request.data.get('emp_pwd_old')
    emp_pwd_new = request.data.get('emp_pwd_new')
    try:
        emp_data=Login.objects.get(Employee_Id=emp_id)
        if(emp_data.Password == emp_pwd_old):
            emp_data.Password = emp_pwd_new
            emp_data.save()
            return Response("Password Changed...")
    except:
        return Response("Failed.......")
    return Response("Failed")




@api_view(['POST'])
def forgot_password(request):
    emp_id = request.data.get('emp_id')
    emp_dob = request.data.get('emp_dob')
    emp_mail = request.data.get('emp_mail')
    try:
        emp_data=Login.objects.get(Employee_Id=emp_id)
        if(emp_data.Date_Of_Birth == emp_dob and emp_data.Mail_Id == emp_mail):
            import smtplib
            sender_email = "sgs.alertsys@gmail.com"
            import base64
            val = b'c2ltY2xhaXIuc2dzQDk0ODczNTQwMzg='
            pwd = base64.b64decode(val).decode('utf-8')
            receiver = emp_mail
            message = 'Hello '+emp_data.Employee_Name+'..\n\n\nYou have requested your password through\n forgot password portal\nAnd your password is '+emp_data.Password+' \n\n\nThis is a system generated mail, Do not Reply.....'
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(sender_email,pwd)
            server.sendmail(sender_email,receiver,message)
            print('mail sent..to '+emp_mail)
            return Response("Password has been sent to your Mail account.")
    except:
        return Response("Failed..Bad Request")
    return Response("Failed - Wrong credentials")

    

@api_view(['POST'])
def register_user(request):
    emp_name = request.data.get('name')
    emp_pass = request.data.get('pass')
    emp_num = request.data.get('num')
    emp_dob = request.data.get('dob')
    emp_addr = request.data.get('addr')
    emp_mail = request.data.get('mail')
    emp_doj = request.data.get('doj')
    query = Login.objects.last()
    emp_id = int(query.Employee_Id)+1
    emp_status = False
    emp_str_id = str(emp_id)
    dict_data = { 
      'Employee_Id' :  emp_str_id,
      'Employee_Name': emp_name,
      'Mail_Id' : emp_mail,
      'Date_Of_Birth' : emp_dob,
      'Mobile_Number' : emp_num,
      'Address' : emp_addr,
      'Password' : emp_pass,
      'Status' : emp_status,
      'Date_Of_Joining' : emp_doj
    }
    serializer = LoginSerializer(data=dict_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
        
    return Response("Failed")



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

@api_view(['GET'])
def product_namelist(request):
    queryset = Products.objects.all().values_list('product_Name')
    l=list()
    for i in queryset:
        l.append(i[0])
    return JsonResponse(l,safe=False)

@api_view(['GET'])
def product_idlist(request):
    queryset = Products.objects.all().values_list('Product_Id')
    l=list()
    for i in queryset:
        l.append(i[0])
    return JsonResponse(l,safe=False)

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



@api_view(['GET'])
def get_product_detils_name(request,Name):
    name=Products.objects.get(product_Name=Name)
    serializer=ProductSerializer(name,many=False)
    return Response(serializer.data)



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


@api_view(['POST'])
def reduce_stock(request):
    pro_id=request.data.get('pro_id')
    pro_qun=request.data.get('pro_qun')
    try:
        pro_data=Products.objects.get(Product_Id=pro_id)
        qun=pro_data.Stock_Balance
        #if(qun<5):
            #re-order stock using stock table
        pro_data.Stock_Balance=qun-int(pro_qun)
        pro_data.save()
        return Response('Stock raduce successes...')
    except:
        return Response('Failed.......')
    return Response('Failed')



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



@api_view(['GET'])
def create_billnum(request):
    bill = Billing.objects.last()
    current_bill=(bill.Bill_No)+1
    return Response(current_bill)



# Sales api views

@api_view(['POST'])
def total_sales(request):
    Sales=Billing.objects.get.all()
    serializer = SalesSerializer(instance=Sales,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Ok")
    return Response("Failed")


@api_view(['POST'])
def sales_add(request):
    serializer = SalesSerializer(data=request.data)
    Current_date = request.data.get('Date')
    total = request.data.get('Sales')
    try:
        Before_Data = Sales.objects.last()
        Before_Date = Before_Data.Date
        if(Before_Date == Current_date):
            Before_Data.Sales += float(total)
            Before_Data.save()
            return Response('Same date add work')
        else:
            if serializer.is_valid():
                serializer.save()
                return Response('new date amount added')
            else:
                return Response('new date but error')
    except:
        return Response('exeption error')




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


#Tax_api
@api_view(['GET'])
def get_all_tax(request):
    tax=Tax.objects.all()
    serializer=TaxSerializer(tax,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_tax_of(request,date):
    tax=Tax.objects.get(Tax_Date=date)
    serializer=TaxSerializer(tax,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def add_tax(request):
    serializer =TaxSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Ok")
    return Response("Failed")
