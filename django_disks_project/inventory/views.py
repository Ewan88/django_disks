from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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
            data = form.cleaned_data
            album = Album(title=data["title"], year=data["year"], stock_level=data["stock_level"], artist=data["artist"])
            album.save()
            return HttpResponseRedirect('')
    else:
        form = AlbumForm()
    
    return render(request, "inventory/create.html", locals())
