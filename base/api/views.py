from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer

@api_view(['GET'])
def getRoutes(request):
    # routes = [
    #     'GET /api'
    #     'GET /api/rooms',
    #     'GET /api/rooms/:id'
    # ]
    name = 'pratik'

    return Response(name)

@api_view(['GET'])
def getRooms(request,id):
    room = Room.objects.get(id=id)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)