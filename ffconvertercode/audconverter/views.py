from django.shortcuts import render, HttpResponse
from .forms import AudFileField
# Create your views here.
def conv(request, slug):

    form = AudFileField()
    return render(request, 'audconverter/home.html',{'slug':slug,'form':form})
    