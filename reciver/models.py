from django.db import models
from withemail.models import Account

# Create your models here.
Bloodgroup =[
    ("A+","A+"), ("A-","A-"),  ("B+","B+"),("B-","B-"),  ("O+","O+"),('O-','O-'), ('AB+','AB+'),('AB-','AB-')
]

Gender = [
    ('M','M'),
    ('F','F')

]

class Reciver(models.Model):
    User                =models.ForeignKey(Account, on_delete=models.CASCADE)
    firstname           =models.CharField(max_length=100)
    middlename          =models.CharField(max_length=100,blank=True)
    lastname            =models.CharField(max_length=100)
    age                 =models.IntegerField()
    contactnumber       =models.IntegerField()
    incident            =models.CharField(max_length=100)
    bloodgroup          =models.CharField(max_length=10,choices=Bloodgroup)
    Gender              =models.CharField(max_length=1,choices=Gender)
    image               =models.FileField(max_length=100,upload_to='patient/')
    location            =models.CharField(max_length=100)
    unit                =models.PositiveIntegerField()
    emergency           =models.BooleanField()
    requiredate         =models.CharField(max_length=100)


    