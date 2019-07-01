from django import forms
from .models import *
from datetime import date

current_year = date.today().year
artists = Artist.objects.all()

class AlbumForm(forms.Form):
    title = forms.CharField(label="Title:", max_length=100)
    year = forms.IntegerField(label="Year:", max_value=current_year)
    stock_level = forms.IntegerField(label="Stock Level:", max_value=100)
    artist = forms.ModelChoiceField(queryset=artists, empty_label='select an artist')