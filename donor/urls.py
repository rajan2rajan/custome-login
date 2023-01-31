from django.urls import path
from .views import *



urlpatterns = [
    path('donorform/',donorform , name= 'donorform'),
    path('donorview/',donorview , name= 'donorview'),
    path('donorupdate/<id>',donorupdate , name= 'donorupdate'),
    path('donoredelete/<int:id>', donordelete, name= 'donordelete'),



]

