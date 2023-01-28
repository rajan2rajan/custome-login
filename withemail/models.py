from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


# our custome manager 
class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError('user must have a email address')
        if not username:
            raise ValueError('user must have a username')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,email,username,password):
        user = self.create_user(
            email= self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user


# our custome model name = Account
class Account(AbstractBaseUser):
    email               =models.EmailField(verbose_name='email',max_length=100,unique=True)
    username            =models.CharField(max_length=100,unique=True)
    first_name          =models.CharField(max_length=100 , blank=True)
    last_name          =models.CharField(max_length=100 , blank=True)
    date_joined         =models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    # the difference between autp_now vs auto_add_now is 
    # auto_add = when data is saved then it change with time but 
    # auto_add_now = when data is saved and doesnot change with time when object is called
    last_login          =models.DateTimeField(verbose_name='last_login',auto_now=True)
    is_admin            =models.BooleanField(default=False)
    is_active           =models.BooleanField(default=True)
    is_staff            =models.BooleanField(default=False)
    is_superuser        =models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True


# model where we store token of password change and logintoken
class Token_data(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    logintoken = models.CharField(max_length=100)
    loginverified = models.BooleanField(default= False)
    passtoken = models.CharField(max_length=100,blank=True)
    passverified = models.BooleanField(default= False)
