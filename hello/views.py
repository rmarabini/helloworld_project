from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting
# Create your views here.


def hello_world(request):
    return HttpResponse("Hello, World!")


def hello_name_old(request, name="World"):
    return HttpResponse(f"Hello, {name}!")


def hello_name_old2(request, name="World"):
    return render(request, "hello/greeting.html", {"name": name})   


def hello_name(request, name="World"):
    # Try to get a greeting for this name
    greeting = Greeting.objects.filter(name=name).first()
    if greeting:
        message = f"{greeting.message}, {greeting.name}!"
    else:
        message = f"Hello, {name}!"

    return render(request, "hello/greeting.html", {"message": message})