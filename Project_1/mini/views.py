from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def home(request):
    return HttpResponse("Hello from mini app! Go to /hello or /echo")

def hello(request):
    context = {
        "name": "Heng",
        "now": datetime.now(),
    }
    return render(request, "mini/hello.html", context)

def echo(request):
    message = ""
    if request.method == "POST":
        message = request.POST.get("message", "")
    return render(request, "mini/echo.html", {"message": message})