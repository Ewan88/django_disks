from django.shortcuts import render
from django.http import HttpResponse
import csv
import os

def index(request):
    csvdata = []
    with open('text/test.csv', mode='r', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csvreader:
            csvdata.append(row)
            
    return render(request, 'csv/index.html', locals())