from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request,'home.html')

def home_about(request):
    return render(request,'about.html')

    
