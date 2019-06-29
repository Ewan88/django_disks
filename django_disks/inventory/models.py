from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=255)

class Album(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    stock_level = models.IntegerField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
