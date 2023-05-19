from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import authenticate
from django import forms
from withemail.models import Account


# user registration form
class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

	class Meta:
		model = Account
		fields = ('email', 'username', 'password1', 'password2', )

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
		except Account.DoesNotExist:
			return email
		raise forms.ValidationError('Email "%s" is already in use.' % account)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
		except Account.DoesNotExist:
			return username
		raise forms.ValidationError('Username "%s" is already in use.' % username)


# password change email form
class Emailform(forms.Form):
	email = forms.EmailField(max_length=100)

	def clean_email(self):
		value = self.cleaned_data['email']
		if Account.objects.filter(email=value).exists():
			return value
		else:
			return forms.ValidationError('this email doesnot exists')


# user detail change after login 
class UserDetailForm(UserChangeForm):
	class Meta:
		model = Account
		fields = ['username','email','first_name','last_name']



# admin detail change after login 
class AdminDetailForm(UserChangeForm):
	class Meta:
		model = Account
		fields = '__all__'


# user login form
class LoginForm(forms.Form):
	email = forms.CharField(max_length=100,widget=forms.EmailInput)
	password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'placeholder':'enter your passowrd here'}))


# form for change password without email 
class ChangepasswordForm(forms.Form):
	password1 = forms.CharField(max_length=15,widget=forms.PasswordInput)
	password2 = forms.CharField (max_length=15,widget=forms.PasswordInput)
	
	def clean_password1(self):
		value1 = self.cleaned_data['password1']
		value2 = self.cleaned_data['password2']

		if value1!=value2:
			raise forms.ValidationError('two password didnot match')
		return value2

class ContactusForm(forms.Form):
	message = forms.CharField(max_length=500 , required= True)


