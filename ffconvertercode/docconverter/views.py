from django.shortcuts import render
from django.shortcuts import render, HttpResponse
import sys
from .forms import ActFileField
from .models import File1
from PIL import Image
import img2pdf
import io
import pypandoc
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

                
                
                formatnames, downloadpath, error = convPdf(fileobjects[0],fileobjects[0].FileField.name, fileobjects,slug)
                print(downloadpath)
                return render(request, 'docconverter/home.html',{'slug':slug,'formatn':formatnames,'form':form,'name':filenames,'download':downloadpath,'error':error})


    form = ActFileField()
    return render(request,"docconverter/home.html",{'slug':slug,'form':form})


def convPdf(firstobject, filename, fileobjects, slug):
        downloadpaths = []
        formatsforfile = []
        if(slug == "PDF"):
                npath = Path("media/")
                
                tempfilepaths = []
                textfromfile = ''
                output = ''
                imgformatname = ['jpeg','jpg','png','bmp','BMP','JPEG','PNG','JPEG']
                firstimageobject = 0   
                error = 0 
                for f in fileobjects:
                        
                        try:
                                try:
                                        nn = f.FileField.name.split('.')[1]
                                except:
                                        nn = ''
                                        

                                if(nn in imgformatname ):
                                        pdffilename = nameForPdf(f.FileField.name)
                                        #pdfdownloadpath = downloadPathForPdf(firstobject)
                                        
                                        if(firstimageobject == 0):
                                                pdfnpath = str(npath/pdffilename)
                                                firstimageobject = f
                                                downloadpaths.append(downloadPathForPdf(f))
                                        else:
                                                dnfilename = nameForPdf(firstimageobject.FileField.name)
                                                pdfnpath = str(npath/dnfilename)

                                        Pim = Image.open(f.FileField)
                                        Pim = Pim.convert("RGB")
                                        imgname = f.FileField.name.split('.')
                                        formatsforfile.append(imgname[1])
                                        imgname = imgname[0]+".jpg"
                                        Pim.save(npath / imgname,format='jpeg')
                                        tempfilepaths.append(str(npath/imgname))
                                        with open(pdfnpath, 'ab') as f1:
                                                try:
                                                        f1.write(img2pdf.convert(tempfilepaths))
                                                except:
                                                        pass
                                        print(tempfilepaths)
                                else:
                                        
                                                formatsforfile.append(f.FileField.name.split('.')[1])
                                                print(str(npath/f.FileField.name))
                                                nameforfile = nameForPdf(f.FileField.name)
                                                downloadpathforfile = downloadPathForPdf(f)
                                                output = pypandoc.convert_file(str(npath/f.FileField.name), 'pdf', outputfile = str(npath/nameforfile))
                                                downloadpaths.append(downloadpathforfile)
                                                print("-----")
                                                print(output)
                                        


                        except:
                                error = 1
                                formatsforfile.append("format not recognized")
                
                
                

                
                

                return formatsforfile, downloadpaths, error

        elif(slug == "DOCX"):
                npath = Path("media/")
                error = 0
                for f in fileobjects:
                        try:
                                formatsforfile.append(f.FileField.name.split('.')[1])
                                docxfilename = nameForDocx(f.FileField.name)
                                docxdownloadpath = downloadPathForDocx(f)
                                output = pypandoc.convert_file(str(npath/f.FileField.name), 'docx', outputfile = str(npath/docxfilename))
                                print(docxfilename)
                                print(docxdownloadpath)
                                downloadpaths.append(docxdownloadpath)
                                
                                
                        except:
                                error = 1
                                formatsforfile.append('format not recognized')

                return formatsforfile, downloadpaths, error
                
        elif(slug=="MD"):
                npath = Path("media/")
                error = 0
                for f in fileobjects:
                        try:
                                formatsforfile.append(f.FileField.name)
                                mdfilename = nameForMD(f.FileField.name)
                                mddownloadpath = downloadPathForMD(f)
                                output = pypandoc.convert_file(str(npath/f.FileField.name), 'md', outputfile=str(npath/mdfilename))
                                downloadpaths.append(mddownloadpath)
                        except:
                                error =1

                return formatsforfile, downloadpaths, error
        elif(slug=='HTML'):
                npath = Path("media/")
                error = 0
                for f in fileobjects:
                        try:
                                formatsforfile.append(f.FileField.name)
                                htmlfilename = nameForHTML(f.FileField.name)
                                htmldownloadpath = downloadPathForHTML(f)
                                output = pypandoc.convert_file(str(npath/f.FileField.name), 'html', outputfile=str(npath/htmlfilename))
                                downloadpaths.append(htmldownloadpath)
                        except:
                                error = 1
                return formatsforfile, downloadpaths, error
                                
   

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


def nameForDocx(filename):
        nameforfile = filename.split('.')
        nameforfile = nameforfile[0]
        docxfilename = nameforfile+'.docx'
        return docxfilename

def downloadPathForDocx(firstObject):
        downloadpath = firstObject.FileField.url
        downloadpath = downloadpath.split(".")
        downloadpath = downloadpath[0] + '.docx'
        return downloadpath

def nameForMD(filename):
        nameforfile = filename.split('.')
        nameforfile = nameforfile[0]
        mdfilename = nameforfile+'.md'
        return mdfilename

def downloadPathForMD(firstObject):
        downloadpath = firstObject.FileField.url
        downloadpath = downloadpath.split(".")
        downloadpath = downloadpath[0] + '.md'
        return downloadpath

def nameForHTML(filename):
        nameforfile = filename.split('.')
        nameforfile = nameforfile[0]
        htmlfilename = nameforfile+'.html'
        return htmlfilename

def downloadPathForHTML(firstObject):
        downloadpath = firstObject.FileField.url
        downloadpath = downloadpath.split(".")
        downloadpath = downloadpath[0] + '.html'
        return downloadpath