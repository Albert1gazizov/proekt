from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home1.html') 

def register(request):
    return render (request,'register.html')

def zkh(request):
    return render (request,'zkh.html')

def gaz(request):
    return render (request,'gaz.html')

def teplo(request):
    return render (request,'teplo.html')

def domofon(request):
    return render (request,'domofon.html')

def signalka(request):
    return render (request,'signalka.html')

def home1(request):
    return render(request, 'home1.html') 

def about(request):
    return render(request, 'about.html') 