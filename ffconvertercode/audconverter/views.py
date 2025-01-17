from django.shortcuts import render, HttpResponse
from .forms import AudFileField
from .models import Aud
import pydub
from django.conf import settings
from pathlib import Path
import os



# Create your views here.
def conv(request, slug):
    if request.method == "POST":
        form = AudFileField(request.method, request.FILES)
        if form.is_valid():
                file = Aud(AudFile = request.FILES['audfile'])
                file.save()
                download, formatn = convertFile(file ,slug)
                path = file.AudFile.url
                print(file)


                return render(request, 'audconverter/home.html', {'slug':slug,'form':form,'path':path,'download':download,'formatn':formatn.upper(),'name':file.AudFile.name})


    form = AudFileField()
    return render(request, 'audconverter/home.html',{'slug':slug,'form':form})


def convertFile(aud,slug):
    newaud = aud.AudFile
    path = aud.AudFile.url
    name = newaud.name
    name= name.split(".")
    npath = Path("media/")
    npath = Path(settings.MEDIA_ROOT)
    print(name)


    if(slug=="WAV"):
        name[0] = name[0]+".wav"
        newaud=pydub.AudioSegment.from_file(aud.AudFile)
        npath = str(npath/name[0])
        newaud.export(npath,format='wav')
        downloadpath = path.split(".")
        return downloadpath[0]+".wav" , name[1]

    elif(slug=="MP3"):
        name[0] = name[0]+".mp3"
        newaud = pydub.AudioSegment.from_file(aud.AudFile)
        npath = str(npath/name[0])
        newaud.export(npath,format='mp3')
        downloadpath = path.split(".")
        return downloadpath[0]+".mp3" , name[1]

    elif(slug=="MP2"):
        name[0] = name[0]+".mp2"
        newaud = pydub.AudioSegment.from_file(aud.AudFile)
        npath = str(npath/name[0])
        newaud.export(npath,format='mp2')
        downloadpath =path.split(".")
        return downloadpath[0]+".mp2", name[1]

    elif(slug == "OGA"):
        name[0] = name[0]+".oga"
        newaud = pydub.AudioSegment.from_file(aud.AudFile)
        npath = str(npath/name[0])
        newaud.export(npath,format='oga')
        downloadpath = path.split(".")
        return downloadpath[0]+".oga", name[1]

    elif(slug=="OGG"):
        name = name[0]+".ogg"
        newaud = pydub.AudioSegment.from_file(aud.AudFile)
        npath = str(npath/name[0])
        newaud.export(npath,format='ogg')
        downloadpath = path.split(".")
        return downloadpath[0]+".ogg", name[1]

    elif(slug=="RAW"):
        name[0] = name[0]+".mp3"
        newaud = pydub.AudioSegment.from_file(aud.AudFile)
        npath = str(npath/name[0])
        newaud.export(npath,format='raw')
        downloadpath = path.split(".")
        return downloadpath[0]+".raw" , name[1]
