from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

rooms = [
    {'id':1,'name':'pratik'},
    {'id':2,'name':'yash'},
    {'id':3,'name':'kkkkk'},
    {'id':4,'name':'yyyyyy'},
]

# rooms = "pyyyyyy"

def home(request):
    props = {'rooms':rooms}
    return render(request,"base/home.html", props ) 
# below id is from url and 
def room(request, id):
    # return render(request,"base/room.html", { 'id' : id }) 
    room = None
    for i in rooms:
        if i['id'] == int(id):
            room = i;
    context = {'room': room}
    return render(request,"base/room.html", context) 
    