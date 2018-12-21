from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from .forms import ActFileField
import img2pdf
# Create your views here.
def conv(request,slug):
    form = ActFileField()
    return render(request,"docconverter/home.html",{'slug':slug,'form':form})