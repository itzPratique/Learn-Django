from django.urls import path
from . import views 
# from django.views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('room/<str:id>/',views.room, name="room"),
    path('createRoom/',views.createRoom, name="create_room"),
    path('updateRoom/<str:id>',views.updateRoom, name="update_room"),
    path('deleteRoom/<str:id>',views.deleteRoom, name="delete_room"),
]
