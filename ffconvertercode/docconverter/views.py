from django.shortcuts import render
from django.shortcuts import render, HttpResponse
# Create your views here.
def conv(request,slug):
    return render(request,"docconverter/home.html",{'slug':slug})