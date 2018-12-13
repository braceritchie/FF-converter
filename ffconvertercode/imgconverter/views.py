from django.shortcuts import render, HttpResponse

# Create your views here.
def conv(request,slug):
    return render(request, "imgconverter/home.html")
