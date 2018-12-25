from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from .forms import ActFileField
from .models import File1
from PIL import Image
import img2pdf
import os
from pathlib import Path
# Create your views here.
def conv(request,slug):
    if request.method == "POST":
        form = ActFileField(request.POST, request.FILES)
        if(form.is_valid()):
            filefield = File1(FileField = request.FILES['file1'])
            filefield.save()
            formatname, downloadpath = convPdf(filefield,filefield.FileField.name)

            return render(request, 'docconverter/home.html',{'slug':slug,'formatn':formatname.upper(),'form':form,'name':filefield.FileField.name,'download':downloadpath})


    form = ActFileField()
    return render(request,"docconverter/home.html",{'slug':slug,'form':form})


def convPdf(filefield, filename):
    imgfileformats = ['png','jpg','jpeg','bmp','JPEG','PNG','JPEG','BMP']
    nameforfile = filename.split('.')
    nameforfile, formatforfile = nameforfile[0], nameforfile[1]
    npath = Path("media/")
    downloadpath = filefield.FileField.url
    downloadpath = downloadpath.split(".")
    downloadpath = downloadpath[0] + '.pdf'
    
    if(formatforfile in imgfileformats):
        Pim = Image.open(filefield.FileField)
        Pim = Pim.convert("RGB")
        pdffilename = nameforfile+'.pdf'
        newname = nameforfile +".jpg"
        Pim.save(npath / newname,format='jpeg')
        with open(npath/pdffilename, 'wb') as f, open(npath/newname, 'rb') as f2:
            
            f.write(img2pdf.convert(f2))
            
    
    return formatforfile, downloadpath