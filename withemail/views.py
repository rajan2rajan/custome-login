from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages

import uuid
from .utils import send_login_token,send_password_token
from django.contrib.auth  import login,authenticate,logout,update_session_auth_hash
from withemail.forms import RegistrationForm,LoginForm,Emailform,UserDetailForm,AdminDetailForm
from .models import Account,Token_data
from donor.models import Donor
from django.contrib.auth.forms import PasswordChangeForm



# custome signup page with email and also send enail in provided email address 
def signup(request ):
    if not request.user.is_authenticated:
        context = {}
        if request.POST:
            form = RegistrationForm(request.POST)
            if form.is_valid():
                data =form.save()
                email = form.cleaned_data['email']
                username = form.cleaned_data['username']
                auth_token = str(uuid.uuid4())
                result = Token_data.objects.create(user = data , logintoken =auth_token)                 
                send_login_token(email,auth_token,username)   
                result.save()             
                messages.info(request,'verify yourself in your email address')
                return redirect('login')
            else:
                context['registration_form'] = form
        else:
            form = RegistrationForm()
            context['registration_form'] = form
        return render(request, 'register.html', context)
    else:
        return HttpResponseRedirect('/home')



# verify the email address while creatin account 
def verify(request, token):
    try:
        data = Token_data.objects.get(logintoken = token)
        # if logintoken is already verified then 
        if data.loginverified:
            messages.info(request,'email already verified')
            return HttpResponseRedirect('/login')
        else:
        # if logintoken is not verified then 
            data.loginverified=True
            data.save()    
            messages.success(request, 'email verified sucessfull')
            return HttpResponseRedirect('/login')
    # if something happen then show exception 
    except Exception as e:
        print(e)
        return HttpResponseRedirect('/login')



# login page with email verification and also authenticate system 
def loginpage(request):
# check weather verified or not
    if not request.user.is_authenticated:
        if request.method=="POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
# from here we are checeking weather email is verified or not if not send messages verify your self
        # admin cannot change password and username              
                if email=="rajan@gmail.com" and password=='R9865177862':
                    user=authenticate(email=email,password=password)
                    login(request, user)
                    return HttpResponseRedirect('/home/')
 
                else:
                    if email=='rajan@gmail.com':
                        messages.success(request,'password doesnot match')
                        return HttpResponseRedirect('/login') 
                    user = Account.objects.filter(email=email).first()
                    if user is None:
                        messages.success(request,'email doesnot exist')
                        return HttpResponseRedirect('/signup')
                    else:

                        name = user.id
                        isverified = Token_data.objects.get(user = name)
                        if isverified.loginverified==True:
                            
                            user = authenticate(email=email, password=password)
                            if user is not None:
                                login(request, user)
                                return HttpResponseRedirect('/home/')
                            else:
                                messages.success(request,'password doesnot match')
                                return HttpResponseRedirect('/login')
                        else:
                            messages.info(request,'please verify your self by clicking in email')
                            return HttpResponseRedirect('/login')
        else:

            form = LoginForm()
        return render(request , 'login.html',{'form':form})
    else:
        return HttpResponseRedirect('/home')



# logout page 
def logoutpage(request):
    logout(request)
    return redirect('login')


# home page 
def home(request):
    if request.user.is_authenticated:
        username=request.user.username
        total = Donor.objects.all().count()
        #  (A+, A-, B+, B-, O+, O-, AB+, AB-)
        Aplus = Donor.objects.filter(bloodgroup='A+').count()
        Aminus = Donor.objects.filter(bloodgroup='A-').count()
        Bplus = Donor.objects.filter(bloodgroup='B+').count()
        Bminus = Donor.objects.filter(bloodgroup='B-').count()
        Oplus = Donor.objects.filter(bloodgroup='O+').count()
        Ominus = Donor.objects.filter(bloodgroup='O-').count()
        ABplus = Donor.objects.filter(bloodgroup='AB+').count()
        ABminsu = Donor.objects.filter(bloodgroup='AB-').count()

        return render(request , 'home.html',{'username':username,
        "total":total,
        'Aplus':Aplus,
        "Aminus": Aminus,
        "Bplus":Bplus,
        "Bminus":Bminus,
        "Oplus":Oplus,"Ominus":Ominus,"ABplus":ABplus,"ABminsu":ABminsu})
    else:
        return redirect('login')



# password changing after authentication 
def oldpassword(request):
    user = request.user
    if request.user.is_authenticated:
        if request.method =="POST":
            form =PasswordChangeForm(user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request ,user)
                messages.success(request,'password change sucessfull')
                return HttpResponseRedirect('/home')

        form = PasswordChangeForm(request.user)
        return render(request , 'oldpassword.html',{'form':form})
    else:
        return HttpResponseRedirect('/login')




# to change userdetail after login for both user and superuser
def detailchange(request):
    if request.method=='POST':
        if request.user.is_superuser ==True:
            form = AdminDetailForm(request.POST, instance = request.user)
        else:
            form = UserDetailForm(request.POST,instance = request.user) 

        if form.is_valid():
            form.save()
            messages.success(request, 'data changed sucessfull')
            return HttpResponseRedirect('/home/')      
    else:
        if request.user.is_superuser==True:
            form = AdminDetailForm(instance = request.user)
        else:
            form = UserDetailForm(instance = request.user)
        
    return render(request, 'detailchange.html',{"form":form})



def aboutus(request):
    if request.user.is_authenticated:
        username=request.user.username
        return render(request,'aboutus.html',{"username":username})
    else:
        return HttpResponseRedirect('/login')

   
    
from django.contrib.auth.decorators import login_required
from .utils import contactsend
from django.core.mail import send_mail
from django.conf import settings

# @login_required
# def contact_us(request):
#     if request.method =="POST":
#         msg = request.POST['message']
#         print(msg)
#         send_mail(
#             msg,
#             settings.EMAIL_HOST_USER,
#             ['rajanbhandari939@gmail.com'],
#             fail_silently=True
#         )
#     return render(request,'home.html')

from .forms import ContactusForm

@login_required
def contact_us(request):
    if request.method == 'POST':
        form = ContactusForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            print(f'Message: {message}')
    else:
        form = ContactusForm()
    
    return render(request, 'home.html', {'contactus': form})


