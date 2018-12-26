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
        filelist = request.FILES.getlist('file1')
        print(filelist)
        if(form.is_valid()):
                fileobjects = []
                filenames = []
                for f in filelist:   
                        ffield = File1(FileField=f)
                        ffield.save()
                        fileobjects.append(ffield)
                        filenames.append(ffield.FileField.name)
                        print(fileobjects)

                
                
                formatnames, downloadpath = convPdf(fileobjects[0],fileobjects[0].FileField.name, fileobjects)
                
                return render(request, 'docconverter/home.html',{'slug':slug,'formatn':formatnames,'form':form,'name':filenames,'download':downloadpath})


    form = ActFileField()
    return render(request,"docconverter/home.html",{'slug':slug,'form':form})


def convPdf(firstobject, filename, fileobjects):
        pdffilename = nameForPdf(filename)
        pdfdownloadpath = downloadPathForPdf(firstobject)
        npath = Path("media/")
        formatsforfile = []
        tempfilepaths = []
        for f in fileobjects:
                Pim = Image.open(f.FileField)
                Pim = Pim.convert("RGB")
                imgname = f.FileField.name.split('.')
                formatsforfile.append(imgname[1])
                imgname = imgname[0]+".jpg"
                Pim.save(npath / imgname,format='jpeg')
                tempfilepaths.append(str(npath/imgname))
                print(tempfilepaths)
                #with open(npath/pdffilename, 'ab') as f1, open(npath/imgname, 'rb') as f2:
                
                #        f1.write(img2pdf.convert(f2))
                
        with open(npath/pdffilename, 'ab') as f1:
                
                f1.write(img2pdf.convert(tempfilepaths))


        return formatsforfile, pdfdownloadpath
   

def nameForPdf(filename):
        nameforfile = filename.split('.')
        nameforfile = nameforfile[0]
        pdffilename = nameforfile+'.pdf'
        return pdffilename

def downloadPathForPdf(firstObject):
        downloadpath = firstObject.FileField.url
        downloadpath = downloadpath.split(".")
        downloadpath = downloadpath[0] + '.pdf'
        return downloadpath
