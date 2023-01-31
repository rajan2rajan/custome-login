from django.db import models


Bloodgroup =[
    ("A+","A+"), ("A-","A-"),  ("B+","B+"),("B-","B-"),  ("O+","O+"),('O-','O-'), ('AB+','AB+'),('AB-','AB-')
]

Gender = [
    ('M','M'),
    ('F','F')

]

# this is model for donor 
class Donor(models.Model):
    firstname               =models.CharField(max_length=100)
    middlename              =models.CharField(max_length=100,blank=True)
    lastname                =models.CharField(max_length=100)
    Gender                  =models.CharField(max_length=1,choices=Gender)
    age                     =models.IntegerField()
    phonenumber             =models.IntegerField()
    # dateofbirth             =models.DateField(blank=True)
    image                   =models.FileField(max_length=100,upload_to='images/')
    bloodgroup              =models.CharField(max_length=10,choices=Bloodgroup)
    timesofdonate           =models.CharField(max_length=200)
    diseases                =models.CharField(max_length=100)
    donatedate              =models.CharField(max_length=100)
    location                =models.CharField(max_length=100)
