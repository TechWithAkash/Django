from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("<h1>Hello World, You are at Chai Aur Django Homepage</h1>")
    
    # return render(request, 'index.html')
    return render(request,'website/index.html ')

def about(request):
    # return HttpResponse("<h1>Hello World, You are at Chai Aur Django Aboutpage</h1>")
    return render(request,'website/about.html')

def contact(request):
    # return HttpResponse("<h1>Hello World, You are at Chai Aur Django COntactpage</h1>")
    return render(request,'website/contact.html')
def login(request):
    # return HttpResponse("<h1>Hello World, You are at Chai Aur Django COntactpage</h1>")
    return render(request,'website/login.html')