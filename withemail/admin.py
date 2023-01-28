from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account,Token_data

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email','username','date_joined','last_login','is_admin','is_staff')
    search_fields = ('email','username')
    readonly_fields = ('id','date_joined','last_login')

    filter_horizontal = ()
    list_filter =()
    fieldsets =()

admin.site.register(Account,AccountAdmin)


# Register for token data
class TokenAdmin(admin.ModelAdmin):
    list_display=['user','logintoken','loginverified','passtoken','passverified']
admin.site.register(Token_data,TokenAdmin)
