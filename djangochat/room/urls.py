from django.contrib import admin 

from django.urls import path
from .views import rooms ,room
urlpatterns = [
    path('',rooms,name="Rooms"),
    path('<slug:slug>/', room, name="room"),
    


]