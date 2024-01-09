from django.shortcuts import render, redirect
# from django.http import HttpResponse
# Create your views here.
from .models import Room
from .forms import RoomForm
from .models import Topic

# rooms = [
#     {'id':1,'name':'pratik'},
#     {'id':2,'name':'yash'},
#     {'id':3,'name':'kkkkk'},
#     {'id':4,'name':'yyyyyy'},
# ]

# rooms = "pyyyyyy"

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(topic__name__icontains=q)
    #i makes sure that the search result is not affected by case-sensitive and 
    #contains ensures that the possible search for eg if py is in query it will return possible POSITIVE output "python" 
    topics = Topic.objects.all()
    context = {'rooms':rooms, 'topics':topics}
    return render(request,"base/home.html", context ) 

# below id is from url and 
def room(request, id):
    # return render(request,"base/room.html", { 'id' : id }) 
    # room = None
    # for i in rooms:
    #     if i['id'] == int(id):
    #         room = i;
    room =  Room.objects.get(id=id)
    context = {'room': room}
    return render(request,"base/room.html", context) 
    
def createRoom(request):
    form = RoomForm()
    if request.method =='POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('home')
        
    context = {'form' : form}
    return render (request,"base/room_form.html", context)

def updateRoom(request, id):
    room = Room.objects.get(id = id)
    form = RoomForm(instance = room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)

    context={'form':form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, id):
    room = Room.objects.get(id = id)

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':room})
   