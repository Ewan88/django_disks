from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello():
    hello = ""
    for y in range (0, 100):
        for x in range (0, 500):
            hello += "Hello "
        hello += "\n"
    return(hello)

def index(request):
    return HttpResponse(hello())
