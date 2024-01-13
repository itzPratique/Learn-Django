from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.
from .models import Room, Topic, Message
from .forms import RoomForm

# rooms = [
#     {'id':1,'name':'pratik'},
#     {'id':2,'name':'yash'},
#     {'id':3,'name':'kkkkk'},
#     {'id':4,'name':'yyyyyy'},
# ]

# rooms = "pyyyyyy"

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method=='POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:    
            messages.error(request, 'User does not exist')

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request , user)
            return redirect('home')
        else:
            messages.error(request, "Username or Password does not exist!")

    context={'page':page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

#using inbuild django usercreation form not making a separate form like login form 
def registerPage(request):
    page ='register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'An error occured during registration')

    context={'form':form}
    return render(request, 'base/login_register.html',context)

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) | 
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )
    #i makes sure that the search result is not affected by case-sensitive and 
    #contains ensures that the possible search for eg if py is in query it will return possible POSITIVE output "python" 
    topics = Topic.objects.all()
    room_count = rooms.count()

    context = {'rooms':rooms, 'topics':topics, 'room_count':room_count}
    return render(request,"base/home.html", context ) 

# below id is from url and 
def room(request, id):
    # return render(request,"base/room.html", { 'id' : id }) 
    # room = None
    # for i in rooms:
    #     if i['id'] == int(id):
    #         room = i;
    room =  Room.objects.get(id=id)
    #messages is Model Message which is linked with Room using foreign key  
    room_messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()
    if request.method == "POST":
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        ) 
        room.participants.add(request.user)
        return redirect('room', id=room.id)

    context = {'room': room, 'room_messages':room_messages,'participants':participants}
    return render(request,"base/room.html", context) 
    
@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()

    if request.method =='POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('home')
        
    context = {'form' : form}
    return render (request,"base/room_form.html", context)

@login_required(login_url='login')
def updateRoom(request, id):
    room = Room.objects.get(id = id)
    form = RoomForm(instance = room)

    if request.user != room.host:
        return HttpResponse('You are not allowed here!')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)

    context={'form':form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def deleteRoom(request, id):
    room = Room.objects.get(id = id)

    if request.user != room.host:
        return HttpResponse('You are not allowed here!')


    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':room})

@login_required(login_url='login')
def deleteMessage(request, id):
    message = Message.objects.get(id = id)

    if request.user != message.host:
        return HttpResponse('You are not allowed here!')


    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':message})
   
   