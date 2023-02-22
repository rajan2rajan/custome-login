from django.contrib import admin
from .models import Donor

# Register your models here.
@admin.register(Donor)
class Donoradmin(admin.ModelAdmin):
    list_display = ['firstname',"middlename" ,"lastname" ,'Gender',  "age" , "phonenumber" , "image" , "bloodgroup" ,  "timesofdonate" ,'diseases',  "donatedate" , "location"] 