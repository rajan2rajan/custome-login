from django import forms
from .models import Reciver
from datetime import datetime,date


class ReciverForm(forms.ModelForm):
    User = forms.CharField(widget=forms.NumberInput)
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'enter your district only'}))
    requiredate = forms.CharField(widget=forms.DateInput,initial=date.today())
    contactnumber = forms.IntegerField(max_value=9999999999,min_value=9100000000)
    class Meta:
        model = Reciver
        # fields = ('firstname','middlename','lastname','age','contactnumber','incident','bloodgroup','Gender','image','location','unit')
        exclude= ('User',)



        # 21766c2c-7336-4242-b911-1deff893c3ff 