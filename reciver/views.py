from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Reciver,ReciverApproved
from .forms import ReciverForm
from django.contrib import messages
import uuid
import os
# from utils import send_email





# this is reqeust form that how people fill the form 
def reciverform(request):
        username = request.user.id
    # if request.user.is_authenticated:
        if request.method=="POST":
            form = ReciverForm(request.POST,request.FILES)
            if form.is_valid():          
                data=form.save()               
                recap = ReciverApproved.objects.create(user=data,isapproved=False)
                recap.save()
                messages.success(request,'we will contact you in short time')
        else:
            form = ReciverForm()
        return render(request, 'reciverform.html',{'form':form,"username":username })
    # else:
    #     return redirect('login')


# for those person who need blood in emergency 
def foremergency(request):
    username = request.user.username
    data = Reciver.objects.filter(emergency = True).order_by('requiredate')
    if request.method=="GET":
        result = request.GET.get('q')
        if result!=None:
            data = Reciver.objects.filter(emergency = True , contactnumber__iexact=result)
            
    return render(request,'foremergency.html',{'form':data,"username":username })


# for those person who doesnot need blood in emergency 
def reciverview(request):
    username = request.user.username
    data = Reciver.objects.filter(emergency = False).order_by('requiredate')
    if request.method=="GET":
        result = request.GET.get('q')
        if result!=None:
            data = Reciver.objects.filter(emergency = False , contactnumber__iexact=result)
            
    return render(request,'reciverview.html',{'form':data,"username":username })


# this is to show all the list that user request for donate other people can also see the  list 
def allperson(request):
    form = Reciver.objects.all()
    return render(request,'allperson.html',{'form':form})



# this is approval done by admin and they get help from the blood 
def approve(request,id):
    user = Reciver.objects.filter(id=id).first()
    result = ReciverApproved.objects.get(user=user)
    isemergency = user.emergency
    
    if result.isapproved==False:
        result.isapproved=True
        result.save()
        auth_token = str(uuid.uuid4())
        email = request.user.email
        user = Reciver.objects.get(id=id)

        # send_email(email,auth_token)
        if len(user.image)>0:
            os.remove(user.image.path)
        user.delete()
        messages.success(request,'information send sucessfull ')

        if isemergency:
            return redirect('foremergency')
        else:
            return redirect('reciverview')
    else:
        return render(request, 'error.html', status=404)


# this is when admin decline the blood request from reciver 
def decline(request,id):
    user = Reciver.objects.get(id=id)
    isemergency = user.emergency
    if len(user.image)>0:
        os.remove(user.image.path)
    user.delete()
    auth_token = str(uuid.uuid4())
    # send_email(email,auth_token)
    messages.success(request,'information send sucessfull ')
    if isemergency:
        return render(request,'foremergency.html')
    else:
        return render(request,'reciverview.html')




