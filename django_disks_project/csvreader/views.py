from django.shortcuts import render
from django.http import HttpResponse
import csv

def index(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="text/test.csv"'

    writer = csv.writer(response)
    writer.writerow(['Row 1', 'Column 1'])
    writer.writerow(['Row 2', 'Column 2'])
    return response