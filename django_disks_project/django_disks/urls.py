from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('csv', include('csvreader.urls')),
    path('', include('inventory.urls')),
    path('admin/', admin.site.urls),
]
