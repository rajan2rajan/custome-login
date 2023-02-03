from django.db import models
from withemail.models import Account
from autoslug import AutoSlugField

# Create your models here.
Bloodgroup =[
    ("A+","A+"), ("A-","A-"),  ("B+","B+"),("B-","B-"),  ("O+","O+"),('O-','O-'), ('AB+','AB+'),('AB-','AB-')
]

Gender = [
    ('M','M'),
    ('F','F')
]


# all the details that are required to get blood 
class Reciver(models.Model):
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
    # sulgdata            =models.SlugField(max_length=11,unique=True,blank=True)



class Database(models.Model):
    user                =models.ForeignKey(Reciver,on_delete=models.PROTECT)
    firstname           =models.CharField(max_length=100)
    middlename          =models.CharField(max_length=100,blank=True)
    lastname            =models.CharField(max_length=100)
    age                 =models.IntegerField()
    contactnumber       =models.IntegerField()
    incident            =models.CharField(max_length=100)
    bloodgroup          =models.CharField(max_length=10,choices=Bloodgroup)
    Gender              =models.CharField(max_length=1,choices=Gender)
    image               =models.FileField(max_length=100,upload_to='storage/')
    location            =models.CharField(max_length=100)
    unit                =models.PositiveIntegerField()
    emergency           =models.BooleanField()
    requiredate         =models.CharField(max_length=100)



# this model is to make reciver approve  
class ReciverApproved(models.Model):
    user            = models.OneToOneField(Reciver , on_delete=models.CASCADE)
    isapproved      = models.BooleanField(default=False) 







    