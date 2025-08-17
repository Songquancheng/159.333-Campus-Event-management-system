from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def frontend(request):
    return render(request, "index.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', include('login.urls')), 
    path('', frontend, name='frontend'),   
]
