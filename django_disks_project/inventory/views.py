from django.shortcuts import render
from django.http import HttpResponse
from inventor.models import *

# Create your views here.
def index(request):
    artists = Artist.objects.get()
    return render(request, "inventory/index.html", locals())
