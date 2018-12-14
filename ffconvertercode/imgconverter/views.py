from django.shortcuts import render, HttpResponse
from .forms import FileField
from .models import Image
# Create your views here.
def conv(request,slug):
    if request.method == 'POST':
        
        form = FileField(request.POST, request.FILES)
        
        if(form.is_valid()):
            
            file = Image(ImageFile = request.FILES['file'])
            file.save()
            path = file.ImageFile.url
            return render(request, "imgconverter/home.html",{'slug':slug,'form':form,'path':path})

    form = FileField()
    return render(request, "imgconverter/home.html",{'slug':slug,'form':form})
