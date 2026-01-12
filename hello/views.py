from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello_world(request):
    return HttpResponse("Hello, World!")


def hello_name_old(request, name="World"):
    return HttpResponse(f"Hello, {name}!")


def hello_name(request, name="World"):
    return render(request, "hello/greeting.html", {"name": name})
    
