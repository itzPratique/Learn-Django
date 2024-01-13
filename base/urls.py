from django.urls import path
from . import views 
# from django.views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('home/', views.home, name="home"),
    path('room/<str:id>/',views.room, name="room"),

    path('createRoom/',views.createRoom, name="create_room"),
    path('updateRoom/<str:id>',views.updateRoom, name="update_room"),
    path('deleteRoom/<str:id>',views.deleteRoom, name="delete_room"),
    path('delete-message/<str:id>',views.deleteMessage, name="delete_message"),
]
