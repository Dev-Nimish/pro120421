from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def view1(request):
    return HttpResponse("<h1>Welcome to the First page</h1>")

def view2(request,email):
    return render(request,"sample.html",context={'email':email,'name':"Nimish"})

def view3(request,name):
    return HttpResponse(f'<h1>Hello Mr. {name} </h1>')
