import imp
from tokenize import group
from unicodedata import name
from django.shortcuts import render
from .models import Chat,Group
# Create your views here.

def index(request):
    room_name=Group.objects.filter(name=name).first()
  
    if room_name:
        pass
    else:
        room_name=Group(name=name)
    room_name.save()
    
    return render(request,'chat/index.html')

def room(request,room_name):
    context = {
            'room_name':room_name
    }
    return render(request,'chat/room.html',context)
