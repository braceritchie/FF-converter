from django.shortcuts import render
from .forms import VidFileField
# Create your views here.
from .models import FileVid
import ffmpeg
from pathlib import Path

def conv(request,slug):
    if request.method == "POST":
        form = VidFileField(request.method, request.FILES)
        filelist = request.FILES.getlist('file1')
        print(filelist)
        if form.is_valid():
            fileobjects = []
            filenames = []
            for f in filelist:
                fileobj = FileVid(FileField = f)
                fileobj.save()
                fileobjects.append(fileobj)
                filenames.append(fileobj.FileField.name)
                
            print(fileobjects)
            print(filenames)
            downloadpaths, formatnames , error = convVid(fileobjects, filenames, slug)
            return render(request, 'vidconverter/home.html',{'slug':slug,'form':form,'name':filenames,'download':downloadpaths,'formatn':formatnames,'error':error})

    form = VidFileField()
    return render(request,'vidconverter/home.html',{'slug':slug,'form':form})


def convVid(fileobjects, filenames, slug):
    downloadpaths = []
    formatnames = []
    error = 0
    npath = Path('media/')
    try:
        if(slug == "MKV"):
                for f in fileobjects:
                        
                        stream = ffmpeg.input(str(npath/f.FileField.name))
                        stream = ffmpeg.output(stream, str(npath/nameForMKV(f.FileField.name)))
                        ffmpeg.run(stream)
                        formatnames.append(f.FileField.name.split('.')[1])
                        downloadpaths.append(downloadPathForMKV(f))

                return downloadpaths, formatnames, error

               
        elif(slug == "MP4"):
                for f in fileobjects:
                       
                        stream = ffmpeg.input(str(npath/f.FileField.name))
                        stream = ffmpeg.output(stream, str(npath/nameForAVI(f.FileField.name)))
                        ffmpeg.run(stream)
                        formatnames.append(f.FileField.name.split('.')[1])
                        downloadpaths.append(downloadPathForAVI(f))
                return downloadpaths, formatnames, error

                
        elif(slug == 'OGG'):
                for f in fileobjects:
                        
                        stream = ffmpeg.input(str(npath/f.FileField.name))
                        stream = ffmpeg.output(stream, str(npath/nameForOGG(f.FileField.name)))
                        ffmpeg.run(stream)
                        formatnames.append(f.FileField.name.split('.')[1])
                        downloadpaths.append(downloadPathForOGG(f))

                return downloadpaths, formatnames, error

        elif(slug == 'WEBM'):
                for f in fileobjects:
                        
                        stream = ffmpeg.input(str(npath/f.FileField.name))
                        stream = ffmpeg.output(stream, str(npath/nameForWEBM(f.FileField.name)))
                        ffmpeg.run(stream)
                        formatnames.append(f.FileField.name.split('.')[1])
                        downloadpaths.append(downloadPathForWEBM(f))
                return downloadpaths, formatnames, error

    except:
            error = 1
            return downloadpaths, formatnames, error

        


    


def nameForMKV(filename):
        nameforfile = filename.split('.')
        nameforfile = nameforfile[0]
        mkvfilename = nameforfile+'.mkv'
        return mkvfilename

def downloadPathForMKV(firstObject):
        downloadpath = firstObject.FileField.url
        downloadpath = downloadpath.split(".")
        downloadpath = downloadpath[0] + '.mkv'
        return downloadpath

def nameForAVI(filename):
        nameforfile = filename.split('.')
        nameforfile = nameforfile[0]
        avifilename = nameforfile+'.avi'
        return avifilename

def downloadPathForAVI(firstObject):
        downloadpath = firstObject.FileField.url
        downloadpath = downloadpath.split(".")
        downloadpath = downloadpath[0] + '.avi'
        return downloadpath

def nameForOGG(filename):
        nameforfile = filename.split('.')
        nameforfile = nameforfile[0]
        oggfilename = nameforfile+'.ogg'
        return oggfilename

def downloadPathForOGG(firstObject):
        downloadpath = firstObject.FileField.url
        downloadpath = downloadpath.split(".")
        downloadpath = downloadpath[0] + '.ogg'
        return downloadpath

def nameForWEBM(filename):
        nameforfile = filename.split('.')
        nameforfile = nameforfile[0]
        webmfilename = nameforfile+'.webm'
        return webmfilename

def downloadPathForWEBM(firstObject):
        downloadpath = firstObject.FileField.url
        downloadpath = downloadpath.split(".")
        downloadpath = downloadpath[0] + '.webm'
        return downloadpath