from django.urls import path
from . import views 
# from django.views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('room/<str:id>/',views.room, name="room")
]
