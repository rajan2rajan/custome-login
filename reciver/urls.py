from django.urls import path
from .views import *



urlpatterns = [
    path('reciverform/',reciverform , name= 'reciverform'),
    path('nonemergency/',reciverview , name= 'reciverview'),
    path("emergency/",foremergency , name= 'foremergency'),
    path("allperson/",allperson , name= 'allperson'),
    path("emergency/<id>",approve , name= 'approve'),
    path("emergency/<id>",decline , name= 'decline'),





]

