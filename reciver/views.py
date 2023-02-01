from django.shortcuts import render,redirect
from .models import Reciver
from .forms import ReciverForm
from django.contrib import messages

# Create your views here.


def reciverform(request):
    # if request.user.is_authenticated:
        if request.method=="POST":
            form = ReciverForm(request.POST,request.FILES)
            if form.is_valid():
                print('hellow')
                form.save()
                messages.success(request,'we will contact you in short time')
        else:
            form = ReciverForm()
        return render(request, 'reciverform.html',{'form':form})
    # else:
    #     return redirect('login')


def reciverview(request):
    form = Reciver.objects.all()
    return render(request,'reciverview.html',{'form':form})
