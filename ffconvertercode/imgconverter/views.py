from django.shortcuts import render, HttpResponse
from .forms import FileField
from .models import Image1
from PIL import Image 
from django.conf import settings
# Create your views here.
def conv(request,slug):
    if request.method == 'POST':
        
        form = FileField(request.POST, request.FILES)
        
        if(form.is_valid()):
            
            file = Image1(ImageFile = request.FILES['file'])
            file.save()
            download = convertFile(file)
            path = file.ImageFile.url
            
            return render(request, "imgconverter/home.html",{'slug':slug,'form':form,'path':path,'download':download})

    form = FileField()
    return render(request, "imgconverter/home.html",{'slug':slug,'form':form})


def convertFile(im):
        newIm = im.ImageFile
        path = im.ImageFile.url
        name = newIm.name
        name = name.split(".")
        print(name)
        Pim = Image.open(newIm)
        rgb_im = Pim.convert('RGB')
        rgb_im.save("media/"+name[0]+".jpg")
        downloadpath = path.split(".")
        return downloadpath[0]+".jpg"
        
