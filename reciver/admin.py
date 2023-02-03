from django.contrib import admin
from .models import Reciver,ReciverApproved

# Register your models here.

class ReciverAdmin(admin.ModelAdmin):
    list_display = ['firstname','middlename','lastname','age','contactnumber','incident','bloodgroup','Gender','image','location','unit','emergency','requiredate']
    
admin.site.register(Reciver,ReciverAdmin)




class ReciverApprovedAdmin(admin.ModelAdmin):
    list_display = ['user','isapproved']

admin.site.register(ReciverApproved,ReciverApprovedAdmin)