from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import Donor
from .forms import DonorForm
from datetime import datetime,date,timedelta
import os
# Create your views here.

# all admin pannel digram 


# this views is to submit form who donate blood 
def donorform(request):
    username = request.user.username
    if request.user.is_authenticated:
        if request.method=="POST":
            form = DonorForm(request.POST , request.FILES)
            if form.is_valid():
                print('hellow')
                form.save()
        else:
            form = DonorForm()
        return render(request, 'donorform.html',{'form':form,"username":username})
    else:
        return redirect('login')


# this view is who donate the bloods and their details  
def donorview(request):
    username = request.user.username
    if request.user.is_authenticated:
        seven_days_age = datetime.now()- timedelta(days=7)
        data = Donor.objects.filter(donatedate__lt = seven_days_age)
        data.delete()
        all = Donor.objects.all()
        return render(request, 'donorview.html',{'form':all,'data':data,"username":username})
    else:
        return redirect('login')
    



# this view is to update the data and their details 

# while doing edit old image is delete automatic so choose again to upload new one 


def donorupdate(request,id):
    username = request.user.username
    if request.user.is_authenticated:
        data = Donor.objects.get(id=id)
        if request.method=="POST":
            if len(request.FILES)!=0:  
                if len(data.image)>0:
                    os.remove(data.image.path)
                    print('image delete sucessfull')
            
            result = DonorForm(request.POST , request.FILES , instance=data)
            if result.is_valid():            
                result.save()
                return redirect('donorview')
        else:
            form = DonorForm(instance=data)
        return render(request,'donorform.html',{'form':form ,"username":username})
    else:
        return redirect('login')




# this view is to delete the data 
def donordelete(request,id):
    if request.user.is_authenticated:
        data = Donor.objects.get(id=id)
        if len(data.image.path)>0:
            os.remove(data.image.path)
            data.delete()

        print('hellow ')
        return redirect('donorview')     
    else:
        return redirect('login')



    
    