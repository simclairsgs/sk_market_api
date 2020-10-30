from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    with open('Frontend/data.json') as jfl:
        data = json.load(jfl)
        #print(data['CompanyDetails'])
        return render(request,'Frontend/home.html',data['CompanyDetails'])