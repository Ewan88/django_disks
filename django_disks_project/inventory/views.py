from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import AlbumForm

# Create your views here.
def index(request):
    artists = Artist.objects.all()
    return render(request, "inventory/index.html", locals())

def create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, "inventory/index.html", locals())
    else:
        form = AlbumForm()
    
    return render(request, "inventory/create.html", locals())
