from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    artists = Artist.objects.all()
    return render(request, "inventory/index.html", locals())
