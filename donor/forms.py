from django import forms
from .models import Donor
from datetime import datetime



class DonorForm(forms.ModelForm):
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'enter your district only'}))
    donatedate = forms.CharField(widget=forms.DateTimeInput,initial=datetime.now())
    phonenumber = forms.IntegerField(max_value=9999999999,min_value=9100000000)
    class Meta:
        model = Donor
        fields = '__all__'

    # def clean_dateofbirth(self):
    #     val = self.cleaned_data['dateofbirth']
    #     # here val is in int form so we had to convert that in string and that string 
    #     # in to datetime.datetime       '2023-01-30'
    #     intostring = str(val)
    #     year = intostring[:4]
    #     month = intostring[4:6]
    #     day = intostring[6:8]
    #     # data = datetime(year=year,month=month,day=day)
    #     date_obj = datetime.strptime(year,"%Y")    
    #     today = datetime.today()
    #     if date_obj>today:
    #         raise forms.ValidationError('enter your correct date of birth')
    #     return val

    def clean_age(self):
        age = self.cleaned_data['age']
        if age>65 or age<17:
            raise forms.ValidationError('you are not elligible to donate the blood')
        return age

    


    



