from django.shortcuts import render
from django.contrib.auth.decorators import login_required  
from django.http import HttpResponse 

# Create your views here.

def home_page(request):
    return render(request,'home.html')

def home_about(request):
    return render(request,'about.html')

@login_required(login_url="/login/")  
def home(request):  
    return HttpResponse('Welcome, <a target="_blank" href="/logout/">logout</a>')      
